# User Interface Documentation

## Overview

ProctorAI's user interface is built using PyQt5 and provides a modern, intuitive interface for productivity monitoring and intervention. The UI is designed to be both functional and aesthetically pleasing, with a focus on user experience.

## Main Components

### 1. Main Window (`ProcrastinationApp`)

#### Initial Screen
- Task input field
- Start button
- Settings button
- Dynamic welcome message
- Stylish background

#### Monitoring Screen
- Real-time status display
- Timer
- Output log
- Task modification options
- Stop button

### 2. Settings Dialog

Configurable parameters:
- AI model selection
- Text-to-speech options
- Timing parameters
- User preferences
- Analysis mode

### 3. Intervention Popup (`FocusPopup`)

Features:
- Full-screen overlay
- Personalized messages
- Challenge system
- Progress tracking

## UI Implementation

### 1. Main Window Layout
```python
def initUI(self):
    self.layout = QVBoxLayout()
    
    # Welcome section
    self.prompt_label = QLabel()
    self.prompt_input = QTextEdit()
    
    # Control buttons
    self.start_button = QPushButton('Start (⌘⏎)')
    self.settings_button = QPushButton('Settings (⌘S)')
    
    # Monitoring elements
    self.running_label = QLabel()
    self.timer_label = QLabel()
    self.output_display = QTextEdit()
```

### 2. Styling

The interface uses modern styling with:
- Custom colors
- Rounded corners
- Dynamic animations
- Responsive layout
- Custom fonts

Example styling:
```python
self.prompt_input.setStyleSheet("""
    QTextEdit {
        border: 1.5px solid #39FF14;
        border-radius: 20px;
        background-color: black;
        color: white;
    }
""")
```

### 3. Event Handling

Key user interactions:
1. Task Input:
   - Text entry
   - Command shortcuts
   - Validation

2. Monitoring:
   - Real-time updates
   - Status changes
   - Timer tracking

3. Interventions:
   - Popup triggers
   - Challenge completion
   - Resume workflow

## Features

### 1. Dynamic Text Display
- Typing animation effects
- HTML formatting
- Multi-line support
- Rich text capabilities

### 2. Real-time Monitoring
- Status updates
- Timer display
- Activity log
- Color-coded output

### 3. User Interaction
- Keyboard shortcuts
- Mouse controls
- Dialog interactions
- Form validation

### 4. Visual Feedback
- Status indicators
- Progress tracking
- Error messages
- Success notifications

## Customization

### 1. Theme Configuration
- Color schemes
- Font settings
- Layout options
- Background images

### 2. Display Options
- Window size
- Text scaling
- Output formatting
- Timer display

### 3. Interaction Settings
- Keyboard shortcuts
- Mouse behavior
- Dialog preferences
- Notification style

## Best Practices

### 1. UI Design
- Maintain consistency
- Use clear hierarchy
- Provide feedback
- Keep it simple

### 2. Performance
- Optimize updates
- Cache resources
- Manage memory
- Handle events efficiently

### 3. User Experience
- Clear navigation
- Intuitive controls
- Helpful feedback
- Graceful errors

### 4. Accessibility
- Keyboard navigation
- Screen reader support
- Color contrast
- Font scaling

## Extension Points

### 1. New Features
- Add custom widgets
- Extend dialogs
- Create new views
- Implement plugins

### 2. UI Customization
- Theme system
- Layout manager
- Style sheets
- Widget templates

### 3. Interaction Patterns
- Custom events
- New shortcuts
- Dialog flows
- Gesture support 