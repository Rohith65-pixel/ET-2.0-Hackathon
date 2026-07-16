# Design of Emergency Shutdown System for Steam Turbo Generator

P. Abiranjan, K. Vinoth, R. Natarajan, B. A. Abhijith Electronics and Instrumentation Engineering, Sri Sairam Engineering College Anna University, Chennai – 600025

Abstract: The general purpose of a generator is to generate electrical power at higher voltages which for industrial applications. It involves large values of voltage and current controls and must be maintained within the prescribed limits to enable safe and profitable running process. In recent years all the controlling processes are carried out by Programmable Logic Controller (PLC) which is programmed to the customer’s requirements. In order to increase the reliability of the plant solid state logic is overcome by automating the power plant using Programmable Logic Controller (PLC). In addition to it a mathematical model of the steam turbo generator has been developed and its non-linear response has been obtained using MATLAB simulation. The voltage and current control can be done very efficiently by the Programmable Logic Controller (PLC) without the requirement of much man power and at reduced costs.

Keywords:Turbine, generator, PLC, MATLAB.

## I.INTRODUCTION

In India, most of the plants are using solid state logic for all its working purposes. It has been an expensive one mainly for the ones in large scales and a simple discontinuity of a wire could mean the failure of the whole system. This paper gives a detailed view about how to change the solid state logic to a much better one, in this case, a PLC controller. PLC has been growing much in industrial part because of its higher reliability and cost effective property. The PLC software used here is “i-Trilogi 6”. In addition to it a MATLAB simulation has been simulated to compare the various controllers and find out the best one for the system. The system taken here is a Turbo-Generator and the shutdown of that system under emergency purposes.

## II.ARCHITECTURE OF A TURBO GENERATOR A. Turbine

A turbine generator, which is sometimes called a turbogenerator, is usually a synchronous generator that is directly connected to the turbine of a steam power plant. Since the turbines at steam power plants that use fossil fuels operate best and most economically at high rotational speeds, turbine generators driven directly by a turbine shaft must also operate at high rotational speeds. The rotational speed n of a turbine generator is given by the equation f = p × n, where f is the AC frequency and p is the number of pole pairs present in the inner part of the steam turbine generator.

Guided by

T. Sathies Kumar

A turbine generator is an electrical machine of the horizontal type. Its excitation winding is embedded in a rotor with non-salient poles; a three-phase armature winding is located in a stator. The rotor experiences the highest mechanical stress and is therefore manufactured as a solid high-quality steel forging. Because of strength considerations, the linear velocity v of any point of the rotor must not exceed 170–190 m/sec. This requirement limits the diameter of the rotor to D = v/πn = 1.2–1.3 m for n = 50 sec-1.

![](images/770b53d8a238d4f5938a321c4ff21470a5b2c6275391ab83cecff17864a0cc30.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/770b53d8a238d4f5938a321c4ff21470a5b2c6275391ab83cecff17864a0cc30.jpg

    ```json
{
  "equipment_names": ["Generator", "Pump"],
  "equipment_tags_identifiers": [],
  "electrical_components": ["Generator"],
  "mechanical_components": ["Pump"],
  "connections_between_components": [
    {
      "type": "fluid",
      "direction": "from pump to generator"
    }
  ],
  "flow_direction": "right-to-left",
  "numerical_values": [],
  "units": [],
  "warning_limits": [],
  "operating_limits": [],
  "labels_and_annotations": ["Generator", "Pump"],
  "maintenance_information": [],
  "operational_information": []
}
```
    

The relatively small rotor diameter results in a relatively large rotor length. The rotor length, however, is limited by the permissible bending of the turbine shaft and does not exceed 7.5–8.5 m. The surface of the rotor contains longitudinal milled slots, in which the coils of the excitation winding are embedded. The coils are held in place by wedges, which enclose the slots, and by large bindings made of nonmagnetic steel, which cover the ends of the winding. The excitation winding is energized by an electrical machine exciter.

## B. Energy Absorption from fluid - Role of Rotor Blades

When high energy fluid (high pressure and high temperature) passes through series of rotor blades, it absorbs energy from fluid and starts rotating, thus it transforms thermal energy in fluid to mechanical energy. So series of such blades which eventually transform thermal energy, are the most vital part of a steam turbine.

![](images/917df67bdba2ca29135d6cb56c38a93b326f9015bae4b3da23fcb41cadcc22cd.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/917df67bdba2ca29135d6cb56c38a93b326f9015bae4b3da23fcb41cadcc22cd.jpg

    ```json
{
  "equipment_names": ["Rotary Kiln", "Cyclone Separator"],
  "equipment_tags_identifiers": [],
  "electrical_components": [],
  "mechanical_components": [
    "Rotary kiln",
    "Cyclone separator",
    "Support structure"
  ],
  "connections_between_components": [
    "Material flow from rotary kiln to cyclone separator"
  ],
  "flow_direction": ["Material flow"],
  "numerical_values": [],
  "units": [],
  "warning_limits": [],
  "operating_limits": [],
  "labels_and_annotations": [],
  "maintenance_information": [],
  "operational_information": []
}
```
    

If you take a close look at one of the blade, it would be clear that a blade is a collection of airfoil cross sections from bottom to top. When flow passes through such airfoils it induces a low pressure on bottom surface and high pressure on top surface of airfoil. This pressure difference will induce a resultant force in upward direction, thus making the blade rotate. So some part of fluid energy will get transformed to mechanical energy of blade. Before analyzing energy transfer from fluid to blade, we will have a close look at energy associated with a fluid.

## C. Energy Associated with a Fluid

A flowing fluid can have 3 components of energy components

• Kinetic energy - Virtue of its velocity

• Pressure Energy - Virtue of its pressure

• Internal Energy - Virtue of its temperature

## D. Generator

A.C. generators or alternators (as they are usually called) operate on the same fundamental principles of electromagnetic induction as D.C. generators.

Alternating voltage may be generated by rotating a coil in the magnetic field or by rotating a magnetic field within a stationary coil. The value of the voltage generated depends on the number of turns in the coil, strength of the field, the speed at which the coil or magnetic field rotates.

According to Faraday's law of electromagnetic induction, when a conductor moves in a magneticfield (thereby cutting the magnetic flux lines), adynamically induced emf is produced in theconductor. The magnitude of generated emf can be given by emf equation of a DC generator. If a closed path is provided to the moving conductor then generated emf causes a current to flow in the circuit.

![](images/d46d32fbe64f474eed7256ca45d00eb583c599c80e115a43a5e94d3ee6e0b4ea.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/d46d32fbe64f474eed7256ca45d00eb583c599c80e115a43a5e94d3ee6e0b4ea.jpg

    1. Equipment names:
   - Magnet
   - Brush

2. Equipment tags and identifiers:
   - N (North pole of the magnet)
   - S (South pole of the magnet)

3. Electrical components:
   - Slip-Rings

4. Mechanical components:
   - None explicitly mentioned in this image.

5. Connections between components:
   - The brush is connected to the slip-rings.
   - The slip-rings are connected to the electrical circuitry, which is not fully visible but implied by the connections shown.

6. Flow direction:
   - The flow of electricity or current is indicated from the brush through the slip-rings and into the electrical circuit (implied).

7. Numerical values:
   - None present in this image.

8. Units:
   - None present in this image.

9. Warning limits:
   - None present in this image.

10. Operating limits:
    - None present in this image.

11. Labels and annotations:
    - Magnet
    - Brush
    - Slip-Rings

12. Maintenance information:
    - None explicitly mentioned in the image, but maintenance of slip-rings and brushes is implied for electrical systems.

13. Operational information:
    - The image shows a basic representation of an electric motor or generator setup with a brush system to connect the rotating part (implied by the slip-rings) to stationary electrical components.
    - The direction of rotation is indicated, suggesting that this could be a DC motor or similar device where the brushes and slip-rings are used for power transfer.

This technical illustration shows an electric motor or generator setup with a brush system. The brush connects to the slip-rings, which in turn connect to the electrical circuitry (implied). The direction of rotation is indicated by the arrow, suggesting that this could be a DC motor or similar device where the brushes and slip-rings are used for power transfer.
    

## E. Interlock

An interlock is a device used to prevent undesired states in a state machine, which in a general sense can include any electrical, electronic, or mechanical device or system. In most applications an interlock is used to help prevent a machine from harming its operator or damaging itself by stopping the machine when tripped. Household microwave ovens are equipped with interlock switches which disable the magnetron if the door is opened. Similarly washing machines will interrupt the spin cycle when the lid is open. Interlocks also serve as important safety devices in industrial settings, where they protect employees from devices such as robots, presses, and hammers. While interlocks can be something as sophisticated as curtains of infrared beams and photodetectors, they are often just switches.

## F. Interlock in Turbine

![](images/9e549e224399dbd3033ce6a7b1f9d86fef528e017add616e9dbac9b9a46625a4.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/9e549e224399dbd3033ce6a7b1f9d86fef528e017add616e9dbac9b9a46625a4.jpg

    ```json
{
  "equipment_names": ["Compressor", "Combustor", "Gas Turbine", "HRSG (Heat Recovery Steam Generator)", "Generator", "Condenser"],
  "equipment_tags_identifiers": {
    "A": "Air",
    "B": "Compressor",
    "C": "Fuel",
    "D": "Gas Turbine",
    "E": "Flue Gas",
    "F": "HRSG (Heat Recovery Steam Generator)",
    "G": "Generator"
  },
  "flow_directions": {
    "A to B": "Air flow into Compressor",
    "B to C": "Compressed air and fuel into Combustor",
    "C to D": "Combustion gases from Combustor to Gas Turbine",
    "D to E": "Gas turbine exhaust to HRSG",
    "E to F": "Flue gas from HRSG to atmosphere",
    "F to G": "Steam flow from HRSG to Steam Turbine and Generator",
    "G to H": "Electric power generation"
  },
  "units": {
    "Air": "",
    "Fuel": "",
    "Gas Turbine": "",
    "HRSG": "",
    "Generator": "kW",
    "Condenser": ""
  }
}
```
      
Interlocked equipment, like motors or valves, is an equipment that has a protection circuit (real or logic) that interdicts the activation of the equipment if at least one danger condition is met.

## A. Description

## III.PLC

A Programmable Logic Controller (PLC) is an industrial computer control system that continuously monitors the state of input devices and makes decisions based upon a custom program to control the state of output devices. Almost any production line, machine function, or process can be greatly enhanced using this type of control system. However, the biggest benefit in using a PLC is the ability to change and replicate the operation or process while collecting and communicating vital information. Another advantage of a PLC system is that it is modular. That is, you can mix and match the types of Input and Output devices to best suit your application.

The first Programmable Logic Controllers were designed and developed by Modicon as a relay re-placer for GM and Landis. These controllers eliminated the need for rewiring and adding additional hardware for each new configuration of logic. The new system drastically increased the functionality of the controls while reducing the cabinet space that housed the logic. The first PLC, model 084, was invented by Dick Morley in 1969. The first commercial successful PLC, the 184, was introduced in 1973 and was designed by Michael Greenberg.

![](images/e525bb7bd2f12e243f6378ae03e622384dac5ebe00a10ff4843dae3435becd33.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/e525bb7bd2f12e243f6378ae03e622384dac5ebe00a10ff4843dae3435becd33.jpg

    ```plaintext
1. Equipment names:
   - Central Processing Unit

2. Equipment tags and identifiers:
   - Inputs (labeled as such)
   - Outputs (labeled as such)

3. Electrical components:
   - Switches (inputs)
   - Motor (outputs, labeled 'M')

4. Mechanical components:
   - None visible in the image.

5. Connections between components:
   - Inputs to Central Processing Unit
   - Central Processing Unit to Outputs

6. Flow direction:
   - From inputs to outputs through the Central Processing Unit

7. Numerical values:
   - Unclear, no numerical values are present.

8. Units:
   - Unclear, no units are present.

9. Warning limits:
   - Unclear, warning limits not indicated.

10. Operating limits:
    - Unclear, operating limits not indicated.

11. Labels and annotations:
    - Inputs
    - Central Processing Unit
    - Outputs

12. Maintenance information:
    - None visible in the image.

13. Operational information:
    - The diagram represents a basic flow of inputs to a processing unit that then produces outputs.
```
    

There are four basic steps in the operation of all PLCs; Input Scan, Program Scan, Output Scan, and Housekeeping. These steps continually take place in a repeating loop. While Ladder Logic is the most commonly used PLC programming language, it is not the only one. The following table lists of some of languages that are used to program a PLC.

## B. Ladder Logic

Ladder Diagram (LD) Traditional ladder logic is graphical programming language. Initially programmed with simple contacts that simulated the opening and closing of relays, Ladder Logic programming has been expanded to include such functions as counters, timers, shift registers, and math operations. A simple example is shown in the below diagram:

![](images/e3e506ed4c13e7971774f01948fa34e083d51b3ea1f76abbc8dd5b92848a77c5.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/e3e506ed4c13e7971774f01948fa34e083d51b3ea1f76abbc8dd5b92848a77c5.jpg

    ```json
{
  "equipment_names": ["PUMP1"],
  "equipment_tags_and_identifiers": [
    {"tag": "SW1"},
    {"tag": "SW2"},
    {"tag": "OVR1"},
    {"tag": "START"},
    {"tag": "X54"},
    {"tag": "X65"},
    {"tag": "PUMP1"},
    {"tag": "%Q100"}
  ],
  "electrical_components": [
    {"type": "switch", "name": "SW1"},
    {"type": "switch", "name": "SW2"},
    {"type": "relay", "name": "OVR1"},
    {"type": "contactor", "name": "START"},
    {"type": "timer", "name": "X54"},
    {"type": "input", "name": "X65"},
    {"type": "output", "name": "%Q100"}
  ],
  "mechanical_components": [],
  "connections_between_components": [
    {"from": "SW1", "to": "OVR1"},
    {"from": "SW2", "to": "OVR1"},
    {"from": "OVR1", "to": "START"},
    {"from": "X65", "to": "EN"},
    {"from": "X65", "to": "SUB"},
    {"from": "X65", "to": "SPEED"},
    {"from": "PUMP1", "to": "ENABLE"},
    {"from": "ENABLE", "to": "%Q100"}
  ],
  "flow_direction": [
    {"direction": "left_to_right", "components": ["SW1", "OVR1", "START"]}
  ],
  "numerical_values": [],
  "units": [],
  "warning_limits": [],
  "operating_limits": [],
  "labels_and_annotations": {
    "EN": "Enable",
    "ENO": "Enable Output",
    "SUB": "Subtract",
    "SPEED": "Speed"
  },
  "maintenance_information": [],
  "operational_information": [
    {"description": "The diagram shows a control circuit for a pump (PUMP1). The switches SW1 and SW2 are connected to an overcurrent relay OVR1, which in turn is connected to the start contactor START. The input X65 is used as an enable signal with ENO and SUB functions, and SPEED is likely related to speed control or monitoring. The output %Q100 is controlled by ENABLE from PUMP1."}
  ]
}
```
      
Functional Block Diagram (FBD) - A graphical language for depicting signal and data flows through re-usable function blocks. FBD is very useful for expressing the interconnection of control system algorithms and logic.

![](images/fcce087582b0f79be591b31cc848655f11efdd1a94e9e3a77827e02e3a4d4edb.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/fcce087582b0f79be591b31cc848655f11efdd1a94e9e3a77827e02e3a4d4edb.jpg

    ```json
{
  "Equipment_names": ["TON", "RS"],
  "Equipment_tags_and_identifiers": {
    "TON": "OnDelay_1",
    "RS": "Alarm_P12"
  },
  "Electrical_components": [
    {"name": "AND"},
    {"name": "TON"},
    {"name": "RS"}
  ],
  "Mechanical_components": [],
  "Connections_between_components": {
    "High_Press": ["IN", "TON"],
    "T#30s": ["PT", "TON"],
    "Enable": ["AND"],
    "Alarm_Clr": ["AND"],
    "Q1": ["TON", "RS"],
    "S": ["RS"],
    "R1": ["RS"]
  },
  "Flow_direction": {
    "High_Press": "IN",
    "T#30s": "PT",
    "Enable": "AND",
    "Alarm_Clr": "AND",
    "Q1": "TON, RS",
    "S": "RS",
    "R1": "RS"
  },
  "Numerical_values": ["30s"],
  "Units": ["seconds"],
  "Warning_limits": [],
  "Operating_limits": [],
  "Labels_and_annotations": {
    "High_Press": "High_Press",
    "T#30s": "T#30s",
    "Enable": "Enable",
    "Alarm_Clr": "Alarm_Clr",
    "Q1": "Q1",
    "S": "S",
    "R1": "R1"
  },
  "Maintenance_information": [],
  "Operational_information": {
    "TON": "OnDelay_1",
    "RS": "Alarm_P12"
  }
}
```
    

A simple functional block diagram is shown above. Here a delay is given with the help of an ON-timer and the enable switch is a AND gate. The output of the timer and AND gate is given as input to the alarm which turns on if the value exceeds the value given in the timer (30seconds). According to the delay, the AND gate will modify the input to the flip flop and thus the output will appear at the over press or an alarm will be initiated by the circuit if something goes wrong or if the time base value is exceeded by the counter. A preset value will be maintained to make comparison with the value of the counter at every cycle.

## C. Implementation

The PLC ladder logic for the interlocks present in the steam turbine is developed using the PLC software i-Trilogi 6. Each rungs are well placed with the normally open and normally closed circuit types in which, even if any of the condition fails for a turbine, the system will shut down safely not enabling the generator to be turned ON.

![](images/927faddb81b3a6528160e6fb297c22465bb81fbd9190d11333f9f053ebd3ee84.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/927faddb81b3a6528160e6fb297c22465bb81fbd9190d11333f9f053ebd3ee84.jpg

    ```plaintext
Equipment names:
- in_p_sk
- shell_temp
- vb_bar
- M_con
- tur_pres
- ok_lamp

Equipment tags and identifiers:
- psi_1 (p08)
- tsh (p11)
- vsh (p12)
- ish (p13)
- psi_2 (p14)

Electrical components:
- pb1, pb2 (outputs)
- r1_gen (output)

Mechanical components:
- Not explicitly listed in the image.

Connections between components:
- in_p_sk -> shell_temp
- shell_temp -> vb_bar
- vb_bar -> M_con
- M_con -> tur_pres
- ok_lamp -> pb1, pb2

Flow direction:
- The flow is from left to right.
- The output of each component (except the last) feeds into the next.

Numerical values and units:
- No specific numerical values or units are visible in the image.

Warning limits and operating limits:
- Not explicitly mentioned in the image.

Labels and annotations:
- Labels for equipment names, tags, and outputs.
- Annotations for connections between components.

Maintenance information:
- Not provided in the image.

Operational information:
- The diagram shows a sequence of measurements or processes from input pressure (in_p_sk) to output pressure (tur_pres).
```
    

Similarly for the lube oil system also, special care is taken to ensure that pressure of the oil is maintained within the set point level. If it exceeds the set point value, then an alarm buzzer will be initiated which causes the first pump to be turned OFF and subsequently the second pump will be turned ON.

![](images/42823c988ce26bea4aaeba22f3efd3d6d00d0f80d6b73ab3e4125f114a8c4723.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/42823c988ce26bea4aaeba22f3efd3d6d00d0f80d6b73ab3e4125f114a8c4723.jpg

    ```plaintext
1. Equipment names:
   - v_span
   - v_close
   - v_open_1
   - v_close_1
   - dp_high_12
   - dp_high_11
   - dp_high_in
   - dp_high_out
   - v3
   - v4
   - alarm1_3
   - alarm2_3
   - pump1_3

2. Equipment tags and identifiers:
   - man (manual)
   - auto (automatic)

3. Electrical components:
   - relays (v_span, v_close, v_open_1, v_close_1)
   - pressure sensors (dp_high_12, dp_high_11, dp_high_in, dp_high_out)
   - alarms (alarm1_3, alarm2_3)

4. Mechanical components:
   - valves
   - pumps

5. Connections between components:
   - v_span to v_close and dp_high_12
   - v_open_1 to v_close_1
   - dp_high_in to dp_high_out
   - v3 to v4
   - alarm1_3 to pump1_3 (indirectly through the flow direction)

6. Flow direction:
   - From manual and auto inputs to relays, pressure sensors, alarms, and pumps.
   - The flow is bidirectional for some components like valves.

7. Numerical values:
   - Unclear

8. Units:
   - PSI (likely for pressure measurements)
   - Unclear for other units

9. Warning limits:
   - dp_high_in
   - dp_high_out

10. Operating limits:
    - Unclear

11. Labels and annotations:
    - v_span, v_close, v_open_1, v_close_1 (valve positions)
    - dp_high_12, dp_high_11, dp_high_in, dp_high_out (pressure measurements)
    - alarm1_3, alarm2_3 (alarms)
    - pump1_3 (pump)

12. Maintenance information:
    - Unclear

13. Operational information:
    - The system appears to be a lube oil interlock system with manual and automatic control.
    - It includes valve positions, pressure measurements, alarms, and pump operation.

```
      
IV.MATLAB

## A. Description

MATrixLABoratory (MATLAB) is a high-level language and interactive environment for numerical computation, visualization, and programming. Using MATLAB, you can analyze data, develop algorithms, and create models and applications. The language, tools, and built-in math functions enable you to explore multiple approaches and reach a solution faster than with spreadsheets or traditional programming languages, such as C/C++ or Java. You can use MATLAB for a range of applications, including signal processing and communications, image and video processing, control systems, test and measurement, computational finance, and computational biology.

## B. Simulink model

The below figure shows the Simulink model of P,PI,PID controllers in MATLAB. The step signal is given as the input and the response is seen in the scope.

![](images/a358ad402c28c690118ba67a24c31d87e75e9128a0ec364d0f7cdf4671247fac.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/a358ad402c28c690118ba67a24c31d87e75e9128a0ec364d0f7cdf4671247fac.jpg

    ```plaintext
1. Equipment names:
   - P Controller
   - Subsystem
   - Transfer Fun2
   - Transfer Fun1

2. Equipment tags and identifiers:
   - Out1, Out2, Out3 (outputs from subsystems)
   - Output1, Output2, Output3, Output4 (final outputs)

3. Electrical components:
   - PID Controller blocks
   - Summing junctions
   - Subsystem blocks
   - Transfer Function blocks

4. Mechanical components:
   - Not applicable in this diagram.

5. Connections between components:
   - Input Signal1 to P Controller → Out1
   - Input Signal2 to P Controller → Out2
   - Input Signal3 to P Controller → Out3
   - Out1, Out2, Out3 to Transfer Fun2/Transfer Fun1

6. Flow direction:
   - From left to right in the diagram.

7. Numerical values:
   - 4s+2 (numerator of Transfer Fun2)
   - 1/s^2 + 1/s (denominator of Transfer Fun2)
   - 4s+2 (numerator of Transfer Fun1)
   - 1/s^2 + 1/s (denominator of Transfer Fun1)

8. Units:
   - Not explicitly stated, but likely in standard engineering units.

9. Warning limits:
   - Not specified in the diagram.

10. Operating limits:
    - Not specified in the diagram.

11. Labels and annotations:
    - INPUT SIGNAL1
    - INPUT SIGNAL2
    - INPUT SIGNAL3
    - P Controller
    - Subsystem
    - Transfer Fun2
    - Transfer Fun1

12. Maintenance information:
    - Not provided in the diagram.

13. Operational information:
    - The system appears to be a control loop with PID controllers for each input signal.
    - Outputs from subsystems are processed by transfer functions before reaching final outputs.
```
      
It offers tight integration with the rest of the MATLAB environment and can either drive MATLAB or be scripted from it. Simulink is widely used in control theory and digital signal processing for multidomain simulation and Model-Based Design.

## C. Implementation

The open loop response curve for the steam turbo generator is shown below. For a step input, the output shoots up and hence to bring back the process curve to the set point, special tuning method such as “Cohen and Coon” method is employed.

![](images/9f4713d3da9de71f247af153d0ae7a215dcd9d731515abf5cd83b4b512f41f2d.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/9f4713d3da9de71f247af153d0ae7a215dcd9d731515abf5cd83b4b512f41f2d.jpg

    ```json
{
  "equipment_names": ["Steam Turbo Generator"],
  "equipment_tags_identifiers": [],
  "electrical_components": [],
  "mechanical_components": [],
  "connections_between_components": [],
  "flow_direction": null,
  "numerical_values": {
    "Amplitude (V)": [0, 1.8],
    "Time (SEC)": [0, 100]
  },
  "units": {
    "Amplitude (V)": "Volts",
    "Time (SEC)": "Seconds"
  },
  "warning_limits": null,
  "operating_limits": null,
  "labels_and_annotations": {
    "OL RESPONSE": "Blue line representing the open-loop response of the steam turbo generator.",
    "SET POINT": "Yellow horizontal line indicating the set point."
  },
  "maintenance_information": null,
  "operational_information": {
    "Description": "The graph shows the open-loop response of a steam turbo generator over time. The blue curve represents how the amplitude (in volts) changes with respect to time, starting from zero and reaching an asymptotic value around 1.8V as it approaches infinity."
  }
}
```
      
The tuning method for the steam turbine is shown below in which a line tangent to the process curve is drawn such that, the line hitting the top of the axis will be brought down to the horizontal axis. Measuring from the origin to the point where the tangent started, gives us the value of delay time (td) and tau can be calculted from the graph below.

![](images/339a4a3b66614b1c19f093f83a9d561b195690d6d1d3248590756360582897ab.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/339a4a3b66614b1c19f093f83a9d561b195690d6d1d3248590756360582897ab.jpg

    ```json
{
  "equipment_names": ["COHEN AND COON TUNING METHOD FOR STEAM TURBO GENERATOR"],
  "equipment_tags_and_identifiers": [],
  "electrical_components": [],
  "mechanical_components": [],
  "connections_between_components": [],
  "flow_direction": null,
  "numerical_values": [
    {"td": "10 sec"},
    {"Tt": "27 - 10 = 17 sec"}
  ],
  "units": ["sec"],
  "warning_limits": [],
  "operating_limits": [],
  "labels_and_annotations": {
    "title": "COHEN AND COON TUNING METHOD FOR STEAM TURBO GENERATOR",
    "x_axis_label": "TIME (SEC)",
    "y_axis_label": "AMPLITUDE (V)"
  },
  "maintenance_information": [],
  "operational_information": []
}
```
      
V. RESULT

The step signal is given as input and after a small time another step signal is added and the set point is tracked. It is observed that the P controller will not settle to the desired set point.PI controller will settle at the desired set point but it will take a long time. PID controller will settle at the desired set point and the settling time will be small when compared to PI controller.

![](images/5c89785e8234fb0ecf9ffb336c9e984a710acc39d5b0d18d83db3924c631a9e3.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\design-of-emergency-shutdown-system-for-steam-turbo-generator-IJERTV4IS040093\images/5c89785e8234fb0ecf9ffb336c9e984a710acc39d5b0d18d83db3924c631a9e3.jpg

    ```json
{
  "equipment_names": ["Steam Turbo Generator"],
  "equipment_tags_identifiers": [],
  "electrical_components": [],
  "mechanical_components": [],
  "connections_between_components": [],
  "flow_direction": [],
  "numerical_values": [0, 150],
  "units": ["V", "SEC"],
  "warning_limits": [],
  "operating_limits": [],
  "labels_and_annotations": [
    "CLOSED LOOP RESPONSE OF STEAM TURBO GENERATOR",
    "AMPLITUDE (V)",
    "TIME (SEC)",
    "P CONTROLLER",
    "PI CONTROLLER",
    "PID CONTROLLER",
    "SET POINT"
  ],
  "maintenance_information": [],
  "operational_information": [
    "The graph shows the closed loop response of a steam turbo generator with different controllers: P, PI, and PID.",
    "The set point is represented by the yellow line at an amplitude of 1V."
  ]
}
```
      
When the controllers become stable, after a small time delay, a step inputis added with the input signal and the set point is varied. Now the system willtrack the setpoint and become stabilized. Here the P, PI, PID Controllers willtrack the change in step input, the P controller will not settle, PI controller willsettle and the PID controller will settle in a short time much before the PI controller settles. Thus by giving a step change, the set point varies and the newset point is tracked by the controller and hence set point tracking is achieved.

## VI.CONCLUSION

The control system developed replaces actual control systems for steam turbo generators as the operating and design philosophies are kept similar to the original ones, but it incorporates those characteristics that modern systems can offer. With little effort, the control system can be easily implanted in other PLC’s. The software modular structure has been prepared to accept the changes of the control strategies. Thus efficiency of a process is improved by providing necessary interlocks using PLC.

## VII. ACKNOWLEDGMENT

We would like to acknowledge our parents, and the staffs of the Department of Electronics and Instrumentation Engineering, Sri Sairam Engineering College, for supporting this study.

## VIII. REFERENCES

1. Maslo K, et al. Gas turbine model using in design of heat and power stations. IEEE Power Tech Proceedings. Vol. 4; Porto; 2001.

2. Nademi H, et al. Robust controller design for governing steam turbine power generators. IEEE International Conference on Electrical. Machines and Systems. Tokyo; 2009.

3. Chen ZX, et al. Modeling and simulation of steam turbine based on multi-modules high temperature gas-cooled reactor. IEEE 8th World Congress on Intelligent Control and Automation (WCICA). Jinan; 2010

4. Pan J, et al. A new non-linear model of steam turbine unit for dynamic analysis of power system. IEEE International Conference on Power System Technology. Hangzhou; 2010.

5. Soon KY, et al. Validated models for gas turbines based on thermodynamic relationships. IEEE Transactions on Power Systems. Vol. 26; Issue 1; 2011.