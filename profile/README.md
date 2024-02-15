
# WVU Team Mountaineers


## About
We're a student led team competing in the highest levels of robotics
Team Mountaineers competes in the University Rover Challenge, a competition which brings in colleges from across the world to complete challenges designed by the Mars Society.

<p align="center">
  <img width=50% src="images/2023URCTeamMountaineers-876x493.jpg" />
</p>


## Watch our System Acceptance Review videos (SAR)
- [WVU Team Mountaineers System Acceptance Review (SAR) for 2023 University Rover Challenge (URC)](https://www.youtube.com/watch?v=u_G0INgx_XA) 
- [WVU Team Mountaineers System Acceptance Review (SAR) for 2022 University Rover Challenge (URC)](https://www.youtube.com/watch?v=4wiPSe8JtRk)
- [WVU Team Mountaineers System Acceptance Review (SAR) for 2021 University Rover Challenge (URC)](https://www.youtube.com/watch?v=WcyxecE9sAE)
- [WVU Mountaineer Robotics System Acceptance Review (SAR) for 2020 University Rover Challenge](https://www.youtube.com/watch?v=45CkzOCeJRA)
- [WVU MRT System Acceptance Review (SAR) for 2019 University Rover Challenge](https://www.youtube.com/watch?v=_PSUZ2FptRo)
- [WVU Team Mountaineers 2018 URC SAR Video](https://www.youtube.com/watch?v=POSIFwnitT0)

## Final Competition Scoring History 

### Historical Scoring 
<p align="center">
  <img src="images/normalized_scores.png" />
</p>

## More Information
- Read more about our [Team Structure](https://urc.orgs.wvu.edu/team-structure)
- See our open-source efforts: [Documentation](https://urc.orgs.wvu.edu/documentation)
- Join the team: [Join Us!](https://urc.orgs.wvu.edu/join-us)
##  Internal Standards & Conventions
- Internally, we utilize github projects to manage each of our subteams.
- As of 2023, a new organizational structure was created and used to ensure maximal modularity of code and as much forward compatability as possible between different years of competition. Our system is designed to introduce very little refactoring across different iterations or types of software systems and architecture we use.
- ### Internal Organizational System Basics:
    - Libraries:
        - Named "<library_name>_lib"
        - A set of code that is independent from ROS and condenses and simplifies the functionality of a device or common operation into one consise library (e.g: "usb_camera_lib", "dc_motor_lib")
    - Packages:
        - Named "<package_name>_pkg"
        - A package following the [standard set by ROS](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html) for ROS packages.
        - These packages generally implement an internal library (as defined above), and external library (e.g.: [opencv](https://opencv.org/)), or code from existing community ROS code (e.g.: [moveit](https://moveit.ros.org/))

<br><br>

By: [Nathan Adkins](mailto:npa0003@mix.wvu.edu) 

Graph generation and source data found under [urc_data](urc_data)
