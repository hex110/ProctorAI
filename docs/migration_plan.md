# Migration Plan

## Current System Analysis

### Existing Components
1. Screenshot Monitoring
   - Periodic screen capture
   - Basic metadata storage
   - Simple file system storage

2. AI Analysis
   - Direct API calls
   - Simple prompt system
   - Basic determination logic

3. Intervention System
   - Full-screen popups
   - Text-to-speech capability
   - Challenge system

4. Configuration
   - YAML-based prompts
   - Command-line arguments
   - Environment variables

## Migration Strategy

### Phase 1: Database Implementation

#### Step 1: Create Database Structure
```sql
-- Activity tracking
CREATE TABLE activities (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    activity_type TEXT,
    metadata JSON,
    screenshot_path TEXT
);

-- Insights storage
CREATE TABLE insights (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    insight_type TEXT,
    content JSON,
    source_activities JSON
);

-- Task tracking
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    created_at DATETIME,
    description TEXT,
    status TEXT,
    metadata JSON
);
```

#### Step 2: Data Migration
1. Create migration script:
```python
async def migrate_existing_data():
    """Migrate existing screenshot and analysis data"""
    screenshots = await collect_existing_screenshots()
    for screenshot in screenshots:
        await db.activities.insert({
            'timestamp': screenshot.timestamp,
            'activity_type': 'screenshot',
            'metadata': extract_metadata(screenshot),
            'screenshot_path': screenshot.path
        })
```

### Phase 2: Code Refactoring

#### Step 1: Refactor Screenshot Handling
```python
# Before
def take_screenshots():
    image = pyscreenshot.grab()
    save_filepath = os.path.join(SCREENSHOT_DIR, "screen_1.png")
    image.save(save_filepath)
    return [save_filepath]

# After
async def capture_activity():
    image = await async_screenshot.grab()
    metadata = await activity_monitor.get_metadata()
    
    return await activity_store.save_activity(
        ActivityData(image, metadata)
    )
```

#### Step 2: Enhance Analysis Pipeline
```python
# Before
def model_pipeline(model, judge_model, user_prompt, total_cost, image_filepaths):
    response = model.call_model(user_prompt, system_prompt, image_filepaths)
    determination = judge_model.call_model(response)
    return determination, total_cost

# After
async def enhanced_pipeline(activity_data: ActivityData):
    # Quick local check
    if activity_monitor.needs_analysis(activity_data):
        # Queue for batch processing
        await analysis_queue.put(activity_data)
        
    # Process batch if ready
    if analysis_queue.ready_for_processing():
        batch = await analysis_queue.get_batch()
        insights = await analyze_batch(batch)
        await insight_store.save_insights(insights)
```

### Phase 3: Feature Addition

#### Step 1: Activity Monitoring
```python
class ActivityMonitor:
    def __init__(self):
        self.trackers = {
            'keyboard': KeyboardTracker(),
            'application': ApplicationTracker(),
            'git': GitTracker()
        }
    
    async def start_monitoring(self):
        """Start all tracking systems"""
        for tracker in self.trackers.values():
            await tracker.start()
    
    async def get_activity_data(self) -> ActivityData:
        """Collect data from all trackers"""
        return ActivityData(
            timestamp=datetime.now(),
            trackers_data={
                name: await tracker.get_data()
                for name, tracker in self.trackers.items()
            }
        )
```

#### Step 2: Memory System
```python
class MemorySystem:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.cache = Cache()
        self.query_builder = QueryBuilder()
    
    async def store_memory(self, data: Any):
        """Store new memory with appropriate indexing"""
        await self.db.store(
            self.prepare_memory(data)
        )
    
    async def query_memory(self, query_type: str, 
                          timeframe: Optional[TimeFrame] = None):
        """Query memory system with efficient indexing"""
        query = self.query_builder.build(query_type, timeframe)
        return await self.db.execute_query(query)
```

### Phase 4: UI Updates

#### Step 1: Add New UI Components
```python
class EnhancedProcrastinationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_enhanced_ui()
    
    def init_enhanced_ui(self):
        """Add new UI components"""
        self.insights_tab = InsightsTab()
        self.progress_view = ProgressView()
        self.query_interface = QueryInterface()
        
        self.tabs.addTab(self.insights_tab, "Insights")
        self.tabs.addTab(self.progress_view, "Progress")
```

## Rollback Plan

### Database Rollback
```python
async def rollback_database():
    """Restore previous state if needed"""
    await db.revert_to_checkpoint('pre_migration')
    await file_system.restore_backup()
```

### Code Rollback
- Maintain compatibility layer
- Keep old file structure
- Version control checkpoints

## Testing Strategy

### Unit Tests
```python
async def test_data_migration():
    """Test data migration accuracy"""
    original_data = await collect_original_data()
    await perform_migration()
    migrated_data = await fetch_migrated_data()
    assert validate_migration(original_data, migrated_data)
```

### Integration Tests
```python
async def test_enhanced_pipeline():
    """Test full enhanced pipeline"""
    activity_data = generate_test_activity()
    await process_activity(activity_data)
    assert verify_pipeline_results(activity_data)
```

## Deployment Steps

1. **Preparation**
   - Backup existing data
   - Create database checkpoint
   - Verify environment

2. **Database Migration**
   - Run schema creation
   - Execute data migration
   - Verify data integrity

3. **Code Deployment**
   - Deploy new components
   - Update configurations
   - Start new services

4. **Verification**
   - Run test suite
   - Verify functionality
   - Monitor performance

## Rollout Strategy

### Gradual Feature Activation
1. Enable data collection
2. Activate analysis pipeline
3. Roll out UI updates
4. Enable advanced features

### Monitoring
- Performance metrics
- Error rates
- User feedback
- Resource usage

## Contingency Plans

### Data Issues
- Backup restoration
- Incremental rollback
- Data recovery procedures

### Performance Issues
- Resource scaling
- Query optimization
- Cache tuning

### API Issues
- Fallback providers
- Rate limit management
- Error recovery 