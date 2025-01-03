# ProctorAI Architecture

## System Components

### 1. User Interface (`user_interface.py`)

The GUI is built with PyQt5 and provides:
- Task input interface
- Real-time monitoring display
- Settings configuration
- Progress tracking
- Intervention popups

Key classes:
- `ProcrastinationApp`: Main application window
- `SettingsDialog`: Configuration interface
- `FocusPopup`: Intervention display

### 2. Core Logic (`main.py`)

Implements the main monitoring and intervention pipeline:

#### Key Functions:
- `model_pipeline()`: Orchestrates AI model analysis
- `control_sequence()`: Manages the monitoring loop
- `procrastination_sequence()`: Handles intervention events
- `parallel_api_calls()`: Manages concurrent AI model calls

#### Pipeline Flow:
1. Screenshot capture
2. AI analysis
3. Determination
4. Intervention (if needed)

### 3. AI Models (`api_models.py`)

Provides a unified interface for multiple AI models:

#### Base Classes:
- `Model`: Abstract base class for all models
- `Conversation`: Abstract base class for conversation handling

#### Implementations:
- `AnthropicModel`: Claude API integration
- `OpenAIModel`: GPT-4V integration
- `GeminiModel`: Google Gemini integration
- `OLlamaModel`: Local LLaVA integration

### 4. Procrastination Events (`procrastination_event.py`)

Manages intervention UI and interactions:

#### Components:
- Full-screen overlay
- Personalized messages
- Challenge system
- Progress tracking

### 5. Utilities (`utils.py`)

Helper functions for:
- Screen capture
- Text-to-speech
- Image processing
- File management

## Data Flow

1. **Input Processing**:
   ```
   User Input -> Task Specification -> Screenshot Capture
   ```

2. **Analysis Pipeline**:
   ```
   Screenshots -> AI Model(s) -> Determination -> Action Decision
   ```

3. **Intervention Flow**:
   ```
   Procrastination Detected -> Generate Messages -> Display Intervention -> User Challenge -> Resume Monitoring
   ```

## Configuration System

### 1. Command Line Arguments
- Model selection
- TTS settings
- Timing parameters
- User preferences

### 2. YAML Configuration (`config_prompts.yaml`)
- System prompts
- User prompts
- Analysis parameters
- Intervention templates

### 3. Environment Variables
Required API keys:
- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `GEMINI_API_KEY`

## Extension Points

The system is designed for easy extension:

1. **New AI Models**:
   - Implement `Model` base class
   - Add model-specific conversation handling
   - Register in model creation factory

2. **Additional Features**:
   - Extend GUI components
   - Add new intervention types
   - Implement custom analysis pipelines

3. **Configuration Options**:
   - Extend settings dialog
   - Add command-line parameters
   - Modify YAML configuration 