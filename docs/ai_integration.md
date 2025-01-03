# AI Integration Guide

## Overview

ProctorAI uses multiple AI models to analyze user activity and generate personalized interventions. The system is designed to be model-agnostic, allowing for easy integration of different AI providers.

## Supported Models

### 1. Claude (Anthropic)
- Primary model: `claude-3-5-sonnet-20240620`
- Capabilities: 
  - Screen analysis
  - Text generation
  - Multi-modal understanding

### 2. GPT-4V (OpenAI)
- Vision-enabled GPT-4
- Capabilities:
  - Image analysis
  - Context understanding
  - Response generation

### 3. Gemini Pro (Google)
- Model: `gemini-1.5-pro`
- Capabilities:
  - Visual analysis
  - Text generation
  - Real-time processing

### 4. LLaVA (Local)
- Local deployment option
- Capabilities:
  - Basic image understanding
  - Text generation
  - No API requirements

## Model Architecture

### Base Classes

1. **Model Abstract Base Class**:
```python
class Model(ABC):
    def __init__(self, model_name):
        self.model_name = model_name

    @abstractmethod
    def call_model(self, user_prompt, system_prompt=None, image_paths=None):
        pass

    def count_tokens(self, system_prompt, user_prompt, assistant_response, image_paths=None):
        pass
```

2. **Conversation Management**:
```python
class Conversation(ABC):
    @abstractmethod
    def __init__(self, user_prompt, system_prompt=None):
        pass

    @abstractmethod
    def add_message(self, message):
        pass
```

## Integration Points

### 1. Model Implementation
To add a new model:
1. Implement the `Model` base class
2. Create corresponding `Conversation` class
3. Add model to the factory function

### 2. Prompt System
Located in `config_prompts.yaml`:
- System prompts
- User prompts
- Role-specific prompts
- Analysis parameters

### 3. Pipeline Integration

The model pipeline consists of:

1. **Initial Analysis**:
```python
response = model.call_model(
    user_prompt, 
    system_prompt=config["system_prompt"], 
    image_paths=image_filepaths
)
```

2. **Determination**:
```python
determination = judge_model.call_model(
    config["user_prompt_judge"]+response, 
    system_prompt=config["system_prompt_judge"]
)
```

3. **Intervention Generation**:
```python
api_params = [
    {"role": "heckler", ...},
    {"role": "pledge", ...},
    {"role": "countdown", ...}
]
api_results = parallel_api_calls(proctor_model, api_params)
```

## Two-Tier Analysis

The system supports a two-tier analysis approach:

1. **Quick Check** (Router Model):
   - Fast initial screening
   - Lower compute cost
   - Higher false positive rate

2. **Detailed Analysis** (Main Model):
   - Triggered by quick check
   - More thorough analysis
   - Higher accuracy

## Best Practices

1. **Model Selection**:
   - Consider latency requirements
   - Balance accuracy vs. cost
   - Account for API limitations

2. **Prompt Engineering**:
   - Keep system prompts focused
   - Use role-specific contexts
   - Maintain consistent formatting

3. **Error Handling**:
   - Implement robust fallbacks
   - Monitor API rate limits
   - Log model responses

4. **Performance Optimization**:
   - Use parallel API calls
   - Implement token counting
   - Cache responses when appropriate

## Configuration

### Environment Setup
Required environment variables:
```bash
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

### Model Parameters
Configurable via settings or command line:
- Model selection
- Analysis frequency
- Confidence thresholds
- Response parameters 