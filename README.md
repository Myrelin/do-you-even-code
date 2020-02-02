# do-you-even-code
Tool that keeps track of time spent coding each day, and language code was written in.

Please see this small presentation to gain some insight into the implementation process, and creation of this tool:
https://drive.google.com/open?id=17vdTBtbEwuUv6qjt39ZdnyAPwfS38BStBoy2E59KznE

Current features:
- Process Checker module that keeps track of all relevant processes
- User can adapt it to their needs, all that is needed is to add processes to be tracked to the process_names list
- Do you even code tool runs the process checker module every five seconds, looking for changes
- Postgres connection ensures all processes are saved to the database, and times updated until the session is closed
- Minimal Flask application displays past and current processes, and whether the session is ongoing

The purpose of this project is to create several tools, with modularity in mind. Users should be able to pick and choose
which modules they want to use, and have the freedom to add additional modules. 
The tool automatically loads all modules it finds in the modules directory, whether they're objects or utility modules.

If a user wishes to add modules, bear in mind that they should be implemented in such a way that only the check() function
will be called from the main tool. Please see Process Checker module for a working example. 

Planned features: 

- Idle timer: A module that checks whether the active window is one of the tracked processes, pauses timer when necessary
- Statistical analysis: Graphical representation of time spent coding in various languages for the past week/month/year.
- (Optional) Desktop application: For users who prefer a startup desktop dashboard to the flask application
- Language identifier: (short-term solution) Determine the coding language via file extension of actively used IDE
                      (long-term solution) Determine the coding language by parsing files used by IDE, and looking for 
                                           language markers
- (Optional) Notification system: Users can enter their e-mail and set up notifications/reminders after x days have passed
  since their last coding session

Warnings: 

The process checker module has root access, to be able to parse running processes. 
  
