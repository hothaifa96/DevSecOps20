
# Project 3:  Smart Office Environment Controller

## Concept
Build a comprehensive office automation system that controls lights, temperature, meeting rooms, parking spots, and monitors employee wellness - like a smart building brain!

## Core Endpoints

### Environmental Controls
- **POST /api/environment/lights/control** - Control office lighting zones
- **GET /api/environment/lights/status** - Get current lighting status
- **POST /api/environment/temperature/set** - Set temperature for zones
- **GET /api/environment/temperature/current** - Get current temperatures
- **POST /api/environment/hvac/schedule** - Schedule HVAC operations
- **GET /api/environment/energy/usage** - Monitor energy consumption

### Smart Meeting Rooms
- **GET /api/meetings/rooms/available** - Check available meeting rooms
- **POST /api/meetings/rooms/book** - Book a meeting room
- **PUT /api/meetings/rooms/{room_id}/extend** - Extend meeting time
- **DELETE /api/meetings/rooms/{booking_id}** - Cancel room booking
- **GET /api/meetings/rooms/{room_id}/equipment** - Check room equipment status
- **POST /api/meetings/rooms/{room_id}/prepare** - Auto-prepare room (lights, projector, etc.)

### Parking Management
- **GET /api/parking/spots/available** - Check available parking spots
- **POST /api/parking/reserve** - Reserve parking spot
- **GET /api/parking/my-reservations** - View my parking reservations
- **POST /api/parking/checkin** - Check into reserved spot
- **GET /api/parking/violations** - Check parking violations
- **POST /api/parking/guest-pass** - Generate guest parking pass

### Employee Wellness Monitoring
- **POST /api/wellness/checkin** - Daily wellness check-in
- **GET /api/wellness/air-quality** - Monitor office air quality
- **GET /api/wellness/noise-levels** - Check office noise levels
- **POST /api/wellness/break-reminder** - Set break reminders
- **GET /api/wellness/ergonomics/check** - Ergonomic workspace analysis
- **POST /api/wellness/mental-health/support** - Access mental health resources

### Automation Rules
- **POST /api/automation/rules/create** - Create automation rules
- **GET /api/automation/rules/active** - View active automation rules
- **POST /api/automation/scenes/create** - Create environmental scenes
- **POST /api/automation/triggers/motion** - Motion-based triggers
- **GET /api/automation/energy-savings** - View automation energy savings

---