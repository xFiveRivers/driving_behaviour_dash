# **Proposal**

## **Motivation and Purpose**

My Role: Data Scientist Working in an Automotive Engineering Position

Target Audience: DIY Vehicle Tuners, Mechanics, Professional Vehicle Engineers

Tuning vehicles is a complicated process and is a process that can be very subjective driver to driver, while also being objective depending on driving scenarios. Whether it be tuning cars for driving the streets or fine-tuning racecars for shaving hundreths of seconds off laptimes, both scenarios require the tuner/engineer to be able to visualze their data to draw conclusions. Since there are so many different metrics that can be measured, it can get very messy to have to manually plot what is desired. Race engineers especially have various sensors that record forces and accelerations strapped all over the vehicle for dynamic analysis. The purpose of this dashboard is to be able to easily visualize the important metrics from observed data to quickly extract and draw conclusions, wasting less time on visualizing and spending more time fine-tuning.

## **Description of the Data**

This dashboard will be created using a dataset that contains different key vehicle measurements for various driving trips and can be found [here](https://www.kaggle.com/datasets/vitorrf/cartripsdatamining). Data regarding engine parameters and vehicle speed has been taking using snapshots of OBD diagnostics data. Vehicle accelerations and gyroscopic velocites are taken from accelerometer data at the same time. Many different parameters and characterisitics are given, however only a select few are relevant for the use case of this dashboard. The following are the data features that will be used:

- Data Timestamp
- Vehicle Speed ($m/s$)
- Transmission Gear
- Engine Load ($\%\ \text{of Max Power}$)
- Total Acceleration ($m/s^2$)
- Engine Speed $\text{(RPM)}$
- Vehicle Pitch $\text{(deg)}$
- Lateral Acceleration ($m/s^2$)
- Car Load
- Rain Intensity
- Visibility

## **Usage Scenarios and Research Questions**

### Usage Scenarios
Marco is a car enthusiast who has recently imported a car for the purposes of tuning it for a racing competition coming up. He wants to explore how changing engine mapping and air-fuel ratios will impact his transmission shifting points relative to his vehicle speed. He also wants to identify a good suspension stiffness to ensure that his car does not lose too much front wheel traction while accelerating by evaluating the vehicle pitch. After collecting his data, Marco moves the data for the trip into the respective folder and will be able to explore different diagnostics of the test drive. He could inspect the Engine Speed vs. Gear Position plot and adjust his engine mapping. Or he might see that there is a high amount of vehicle pitch and stiffen the suspension to keep front-wheel grip through corners.

Monica is a diagnostic engineer for a racing team and has fitting a car with many different sensors to extract inforation for test laps. She is taked with identifying the driving characteristics of a driver in varying conditions of rain. Taking past test lap data, she filters the plots by rain intensity and vehicle load. From the vehicle speed plots she can see that the driver has much less confidence in the vehicle by being slower around the corners. The lateral accleration plots also show that the vehicle has a much higher tendency to spin when the pitch of the vehicle spikes, so it might help to reduce the suspension stiffness and change the toe angles of the rear tires.