![](images/a5aa68779eb9f4629f3b2e88fdd91d69f6a6b4d162f26789efb1e7ebf56e473f.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/a5aa68779eb9f4629f3b2e88fdd91d69f6a6b4d162f26789efb1e7ebf56e473f.jpg

    ```plaintext
1. Equipment names:
   - Cylinder (M)
   - Amplifier (G)

2. Equipment tags and identifiers:
   - No specific tags or identifiers are visible.

3. Electrical components:
   - Amplifier (G)
   - Summing junction

4. Mechanical components:
   - Cylinder (M)

5. Connections between components:
   - Cylinder (M) to amplifier (G)
   - Amplifier (G) to summing junction
   - Summing junction back to cylinder (M)

6. Flow direction:
   - The flow is from the cylinder (M) through the amplifier (G) and then into a summing junction, which returns the signal back to the cylinder (M).

7. Numerical values:
   - No numerical values are visible.

8. Units:
   - No units are visible.

9. Warning limits:
   - No warning limits are visible.

10. Operating limits:
    - No operating limits are visible.

11. Labels and annotations:
    - Amplifier (G)
    - Summing junction

12. Maintenance information:
    - No maintenance information is provided in the image.

13. Operational information:
    - The system appears to be a feedback loop where the output of the amplifier (G) is summed with an input signal, and this sum is fed back into the cylinder (M).
```
    

# Maintenance and operational patterns in thermal power generation

A cost assessment of the relation between maintenance and operational patterns of thermal power plants

Master’s thesis in

Master Programme Sustainable Energy Systems &

Master Programme Production Engineering

JOHAN EGELAND WILLIAM FLODIN

Department of Space, Earth and Environment CHALMERS UNIVERSITY OF TECHNOLOGY Gothenburg, Sweden 2019

Master’s thesis 2019

# Maintenance and operational patterns in thermal power generation

Methodology development for maintenance cost estimation

JOHAN EGELAND WILLIAM FLODIN

![](images/713589dc22d479317b81521fc20ce1f8463f78a92e8898bf1f31ab787d9b0647.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/713589dc22d479317b81521fc20ce1f8463f78a92e8898bf1f31ab787d9b0647.jpg

    ```plaintext
AVANCEZ
1829

Equipment names:
- Compass
- Hammers (two)
- Wreath of leaves

Equipment tags and identifiers: None visible.

Electrical components: None visible.

Mechanical components:
- Compass
- Hammers (two)

Connections between components:
- The compass is at the top.
- Two hammers are positioned below the compass, with one on each side.

Flow direction: Not applicable as this image does not depict a flow diagram or process.

Numerical values:
- 1829

Units: None visible.

Warning limits: None visible.

Operating limits: None visible.

Labels and annotations:
- AVANCEZ
- 1829

Maintenance information: None visible.

Operational information: None visible.
```
    

CHALMERS UNIVERSITY OF TECHNOLOGY

Department of Space, Earth and Environment Division of Energy Technology Chalmers University of Technology Gothenburg, Sweden 2019

Maintenance and operational patterns in thermal power generation

# Methodology development for maintenance cost estimation JOHAN EGELAND WILLIAM FLODIN

## © JOHAN EGELAND, WILLIAM FLODIN 2019.

Supervisors: Dr. Rubén Mocholí Montañés, Department of Space, Earth and Environment Dr. Maheshwaran Gopalakrishnan, Department of Industrial and Materials Science

Examiner:   
Associate Professor Dr. Fredrik Normann, Department of Space, Earth and Envi  
ronment

Master’s Thesis 2019

Department of Space, Earth and Environment

Division of Energy Technology

Chalmers University of Technology

SE-412 96 Gothenburg

Telephone +46 31 772 1000

Cover: A clip-art factory housing a simplified steam cycle with smart technology connecting machinery and processes for monitoring maintenance.

Typeset in LAT<sub>E</sub>X Printed by Chalmers Reproservice Gothenburg, Sweden 2019

# Maintenance and operational patterns in thermal power generation

Methodology development for maintenance cost estimation   
JOHAN EGELAND   
WILLIAM FLODIN

Department of Department of Space, Earth and Environment Chalmers University of Technology

## Abstract

With increasing shares of solar and wind generation in the power system, the understanding of power generation system as we know it today, needs to be reassessed. Wind and solar power, known as the non-dispatchable generation, are likely to impact the net load on the grid and dispatchable power production, typically thermal power plants, will face more frequent starts and stops and volatile operational patterns. This is expected to cause tougher conditions for the plant and result in more critical wear on the equipment, which must be considered and accounted for.

This master’s thesis develops a method to evaluate maintenance costs depending on the operational pattern - in terms of the number and types of start-ups - of a steam cycle. The work focus on the steam turbine rotor but could be applied also to other critical components of the plant. The method includes a rotor model to perform transient simulations of the rotor temperature during start-ups. The rotor temperature was then related to thermal stresses and life expenditure of the rotor, which are typical input parameters to estimate maintenance costs from an LCC-perspective. The method may be applied to evaluate the influence of energy system scenarios, process designs, and maintenance policies.

To exemplify, this work evaluates the maintenance cost of the rotor for six defined scenarios, four maintenance policies, i.e. failure-based, time-based, condition-based and opportunity-based maintenance, and three types of labour services, internal, external and contract service. The examples illustrate how the maintenance costs may be related to the number of starts and that the proposed method may be provide initial support to the initial discussions on the maintenance of thermal power plant components.

Keywords: Maintenance, Production, Life Cycle Cost, LCC, Power generation, Transient operation, Steam turbine, Flexible operation

## Acknowledgements

This thesis is a result of many hours of eagerness, progress, doubtfulness, confusion and a lot of happiness. Many hours have been spent on thinking, understanding and intense discussions. And also to get to know where we were actually expected to end up. Eventually, between all high and lows, where time sometimes flew and sometimes stood still, this master’s thesis was at last produced. The result is a thesis that is a joint between two fields of engineering and is merging knowledge from two master’s programs. Collaboration made it possible and we are thankful for the belief in success as well as all the new knowledge we have gained. As five years at Chalmers have lastly come to an end, we would also like to emphasize our appreciation to all of our friends and classmates making our time at Chalmers a pleasure. A big thank you to all of you!

We would also like to send a special thanks to our examiner Fredrik Normann for appointing us the thesis topic and for your genuine interest in our work. Our greatest appreciation is also devoted to our two supervisors Rubén Mocholí Montañés and Maheshwaran Gopalakrishnan who have actively taken part of our job and provided us with experienced knowledge and valuable insights since day one. You have made sure that we are challenged enough while still ensuring that we can provide results on time and on reasonable grounds. You have also shown your interest in our work by helping out on all levels. A warm thank you to you!

Lastly, we would like to thank our families and loved ones for being our cornerstones during our years at Chalmers. You have been there for us when school has been our life and you have made sure that there are also other things in life as well, other than ordinary, partial and stochastic diferential equations. Love to you!

We hope that our work on maintenance costs in relation to operational patterns in thermal power plants will help to continue to build bridges across the fields of production engineering and energy technology. We have enjoyed to be working in the two fields and we hope more student will do the same. Maybe this is a "start-up" of something new.

Thank you,

Johan Egeland

William Flodin

Gothenburg, May 2019

## Contents

List of Figures xi   
List of Tables xiii   
Nomenclature xv   
1 Introduction 1   
1.1 Background 1   
1.2 Aim and purpose 3   
1.3 Delimitations 3   
1.4 Specification of problem 3   
1.5 Thesis outline 4   
2 Theory on Production and Energy Systems 5   
2.1 Electrical grid 6   
2.2 Electricity market . 7   
2.3 Electrical power demand and load types 7   
2.4 Maintenance classification 9   
2.4.1 Maintenance concepts 9   
2.4.2 Maintenance policies 10   
2.4.3 Maintenance actions 10   
2.5 Maintenance as a service 11   
2.5.1 Internal crew 11   
2.5.2 External service 11   
2.5.3 External service with framework contract . 11   
2.6 Dependability 12   
2.6.1 Reliability 12   
2.6.2 Maintainability 13   
2.6.3 Maintenance support 13   
2.7 Power generation by steam turbines 14   
2.7.1 Steam turbine fundamentals 14   
2.7.2 Maintenance on steam turbines 19   
2.8 Cost calculations on maintenance 20   
2.8.1 Failure-based maintenance 21   
2.8.2 Time-based maintenance 21   
2.8.3 Condition-based maintenance 22   
2.8.4 Opportunity-based maintenance 22   
3 Methodology 23   
3.1 Development of methodology framework 24   
3.1.1 Steam turbine simulation and thermal stresses . 25   
3.1.2 Equivalent operating hours 26   
3.1.3 Reliability due to fatigue 26   
3.1.4 Maintenance cost calculations 27   
3.1.5 Result presentation 27   
3.2 Determination of data input 28   
3.2.1 Material properties 28   
3.2.2 Steam turbine data 29   
3.2.3 Equivalent operating hours data . 30   
3.2.4 Maintenance cost data 30   
3.3 Scenarios and results analysis 33   
4 Results 35   
4.1 Thermal stresses on the steam turbine rotor 36   
4.2 Equivalent operating hours calculations 38   
4.3 Reliability analysis 39   
4.4 LCC-calculations on maintenance costs 41   
5 Discussion 47   
5.1 Methodology and sensitivity 47   
5.2 Experience for future work 50   
6 Conclusion 53   
7 Future work 55   
References 57   
A Appendix - Interview questions I

## List of Figures

2.1 Power demand and load curves 8   
2.2 Maintenance levels 9   
2.3 Factors in dependability 12   
2.4 Illustration of a steam cycle 14   
3.1 Visual mapping of methodology framework . 24   
3.2 Start-up curves 29   
4.1 Temperature distributions of start-ups 36   
4.2 Start-up stress-profiles 37   
4.3 S-N curve for AISI 10 . 37   
4.4 Reliability curves for each start-up type 40   
4.5 Visualization of internal maintenance costs 43   
4.6 Visualization of external maintenance costs 44   
4.7 Visualization of contract maintenance costs 45

## List of Tables

2.1 Maintenance policies . 10   
2.2 Biot numbers and roots to Bessel function 17   
3.1 Material properties for AISI 10 28   
3.2 Steam turbine start-up conditions 29   
3.3 LCC data input 31   
3.4 Scenario definitions 34   
4.1 Start-up results 38   
4.2 Results on EOH for each scenario 39   
4.3 Weibull parameters . 39   
4.4 Numbers on reliability parameters 40   
4.5 LCC-results for the diferent scenarios. 42

## Nomenclature

<table><tr><td colspan="2">Abbreviations</td></tr><tr><td>CBM</td><td>Condition Based Maintenance</td></tr><tr><td>EOH</td><td>Equivalent Operating Hours</td></tr><tr><td>EXT</td><td>External maintenance service</td></tr><tr><td>FBM</td><td>Failure Based Maintenance</td></tr><tr><td>FWC</td><td>Framework of an annual contract</td></tr><tr><td>INT</td><td>Internal maintenance service</td></tr><tr><td>KPI</td><td>Key Performance Indicator</td></tr><tr><td>LCC</td><td>Life Cycle Cost</td></tr><tr><td>MTTF</td><td>Mean Time To Failure</td></tr><tr><td>MTTR</td><td>Mean Time To Repair</td></tr><tr><td>OBM</td><td>Opportunity Based Maintenance</td></tr><tr><td>OEM</td><td>Original Equipment Manufacturer</td></tr><tr><td>PSS</td><td>Product-Service System</td></tr><tr><td>TBM</td><td>Time Based Maintenance</td></tr></table>

<table><tr><td> $\alpha _ { d i f f }$ </td><td>Thermal diffusivity</td><td> $[ \mathrm { m ^ { 2 } / s } ]$ </td></tr><tr><td> $\alpha _ { e x p }$ </td><td>Thermal expansion</td><td> $[ { } ^ { \circ } \mathrm { C } ^ { - } 1 ]$ </td></tr><tr><td> $\dot { m }$ </td><td>Mass flow rate</td><td> $[ \mathrm { k g / s } ]$ </td></tr><tr><td> $\epsilon$ </td><td>Elongation</td><td>[% strain]</td></tr><tr><td> $\eta _ { T }$ </td><td>Isentropic turbine efficiency</td><td>H]</td></tr><tr><td> $\lambda$ </td><td>Thermal conductivity</td><td> $[ \mathrm { W } / ( \mathrm { m } ^ { \circ } \mathrm { C } ]$ </td></tr><tr><td> $\rho$ </td><td>Density</td><td> $\mathrm { [ k g / m ^ { 3 } ] }$ </td></tr><tr><td> $\sigma _ { z }$ </td><td>Axial stress</td><td> $\mathrm { [ M P a ] }$ </td></tr><tr><td> $\theta$ </td><td>Dimensionless temperature</td><td>[-]</td></tr><tr><td> $\zeta _ { n }$ </td><td>Roots to the Bessel function</td><td>[-]</td></tr><tr><td> $B i$ </td><td>Biot number</td><td>[-]</td></tr></table>

$C _ { n }$ Roots to the Bessel function [-]   
$C _ { p }$ Specific heat capacity $[ \mathrm { J / ( k g ^ { \circ } C ) }$   
$E$ Young’s modulus $\mathrm { [ P a ] }$   
$F o$ Fourier number [-]   
$h$ Enthalpy $[ \mathrm { k J / k g } ]$   
$H T C$ Convective heat transfer coeficient $\mathrm { [ W / ( m ^ { 2 \circ } C ) ] }$   
$J _ { 0 }$ First order of the Bessel function [-]   
$K$ Correction factor [-]   
$k _ { c }$ Stress correction factor [-]   
$N u$ Nusselt number [-]   
$p$ Pressure [Pa]   
$P _ { e l }$ Electric power output [MW]   
$P r$ Prandtl number [-]   
$r$ Radius [m]   
$R e$ Reynolds number [-]   
$T$ Temperature [°C]   
$t$ Time [h]   
$v$ Poisson’s ratio [-]   
Variables for maintenance cost model   
$\beta$ Shape parameter of a Weibull distribution [-]   
$\eta$ Scale parameter of a Weibull distribution [-]   
$\psi$ Time in operation at a specific given load [h]   
$\sigma _ { F W C }$ Coeficient considering warranties [%]   
$\sigma _ { S P }$ Factor neglecting spare part change [%]   
$\tau _ { l i f e }$ Expected lifespan of the rotor [h]   
$\xi$ Fraction of interventions causing downtime [%]   
$A$ Availability [%]   
$a$ Time coeficient of EOH [h]   
$b$ Coeficient given a specific operating regime [-]   
$C _ { C B M }$ Cost of CBM-policy [SEK]   
$C _ { C D }$ Cost due to collateral damage [SEK]   
$C _ { F B M }$ Cost of FBM-policy [SEK]   
$C _ { L P }$ Cost of lost production [SEK]   
$C _ { O B M }$ Cost of OBM-policy [SEK]   
$C _ { S P }$ Cost of spare part [SEK]   
$C _ { T B M }$ Cost of TBM-policy [SEK]   
$E _ { T B M }$ Inspection interval for a TBM-policy [h]   
$E O H$ Equivalent Operating Hours [h]   
$F$ Fixed costs (consumables, machinery etc.) [SEK]   
$f ( t )$ Probability density function as a function of time [%]   
$L$ Labour cost [SEK]   
$M D T$ Mean delay time [h]   
$M T T F$ Mean Time To Failure [Cycles]   
$M T T R$ Mean Time To Repair [Cycles]   
$N$ Number of cycles to failure [-]   
$n$ Number of start-ups [-]   
$O H$ Operating hours [h]   
$p _ { 1 }$ Fraction of life where it is possible to detect failures [%]   
$p _ { 2 }$ Fraction of failures happening without being recognized [%]   
$R ( t )$ Reliability as a function of time [%]   
$S D T$ Spare part acquisition delay time [h]   
$t$ Time [h]   
$T M$ Time needed to carry out preventive task [h]   
$Y$ Years in service [Years]   
$Z$ Damageability parameter [-]

# Introduction

The availability of electricity in developed countries has become an obvious resource, constantly available in our power outlets. This requires reliable energy production, where it is made sure that the producing equipment can provide its function whenever demanded. This emphasize the need for proper maintenance.

This thesis studies the relationship between maintenance costs and operational patterns at thermal power plants. A background is following along with the aim of the thesis, delimitations and a specification of issues under investigation.

## 1.1 Background

The energy market and its afiliated energy systems have seen rapid development in recent years towards an increased share of non-dispatchable renewable energy sources such as wind and solar power generation [1]. This trend has initiated discussions on the role of dispatchable large scale thermal power generators as well as the consumers in the system [2]. As some electricity markets has been deregulated and opened up for private actors, the competitive landscape and the actual power generation is changing.

On the traditional energy market, there was a distinct classification of producer and consumer, connected on a centralized network. Today, the consumer could also be the producer, by selling redundant self-produced electricity to the market [2]. Along with a varying electricity demand from the customers and the varying power generation of non-dispatchable energy sources, this is creating strong irregularities and discontinuous operational patterns at the power generation plants [3]. The production must also constantly be matched with the demand as a fundamental requirement [2]. This is relatable to a chase strategy typically known in capacity planning within production environments [4], with the diference that the electricity market is changing the demand in real-time. As changes in the load appear, the production must follow and deliver what is being demanded. Without the continuous supply and availability of electricity in our outlets, many of our societal functions would not function properly. It is thus important to maintain and care for the equipment making the power generation, as well as heat generation possible and its future functioning in the society.

With a varying load in the power system, the operational pattern of power units must be varying as well, as overproduction could impact on profits in terms of unnecessary usage of resources as well as the fact that the power grid cannot handle a significant overproduction either, and the plant could even be paid to decrease production. The varying operating cycles are followed by an increase of start-and-stops, severe transients and possible longer downtimes of the thermal power plants. This is often raised as a concern from the industry, which is generally used to continuous operation patterns [5]. This type of changed production pattern is expected to impact on the lifetime of critical components in the equipment due to an increased probability of failure, caused by mechanisms such as creep and thermal-mechanical fatigue loadings [6], which might lead to additional unplanned maintenance costs and unavailability [3].

As industrial maintenance practices, as well as research in maintenance of production systems, has undergone advancement the last years, it has now moved to be an important part in business strategies [7]. As an example, in manufacturing, maintenance has become a central core of the production system [8], as research shows that optimization of maintenance can increase the performance of the production systems [9] and gain economical benefits [7]. By regarding a power plant as a production system, that is transforming an input into an output, the same principles of maintenance are possible to apply.

With the possibility of highly volatile electricity prices on the future electricity market, it is believed that processes that can work eficiently during transient or intermittent operations are needed and thus the maintenance perspective cannot be ignored. Vishnu and Regikumar [10] are stating that the maintenance cost can reach as high as 40% of the total operational cost of a plant, which could be impacting on possible profits. This project aims at estimating and understanding the relationship between maintenance costs and operational patterns in thermal power plants, and act as a support in the discussions. The true understanding of maintenance in a production system could help companies to stay competitive on their market.

Research on maintenance and operational patterns is also believed to support the operator experience by the giving of a support basis for decisions on maintenance actions. With the possibility of making economical maintenance decisions in aspects of lifetime extension, it could be possible to extend the lifetime of machinery and minimize costs. As this could help to decrease used parts and resources, it could further decrease environmental impact and support eficient energy production in general, making our future more sustainable.

For the reader interested in a more comprehensive background to the thesis, it is referred to lifetime assessment research by Banaszkiewicz, Moroz et al., Benato et al., Venkatesh et al., Musyafa et al. and Grosso et al. [11]–[16]. And for topics related to steam turbine costs on maintenance, it is referred to Keatley et al., Stoppato et al., Aminov et al. and Kumar et al. [3], [17]–[19].

## 1.2 Aim and purpose

The aim of the project is to develop a cost assessment methodology for how the maintenance cost varies based on the number of starts of a thermal power plant. This will be done by combining theory and methods from the fields of energy technology and production engineering, that will help to simulate, estimate and understand the relationship between maintenance and operational patterns at thermal power plants. The relation is assessed in terms of life-cycle cost (LCC) for diferent maintenance policies and services related to defined scenarios.

The purpose of the development of the methodology is sought to be the beginning of a supporting tool that can help initial discussions of maintenance strategies at thermal power plants. With further development and accurate data, it is thought that the methodology and tool could help to enable cost eficiency in thermal power production in long-term perspectives and support the operator experience in maintenance decisions.

## 1.3 Delimitations

The principal delimitation in the project is the focus on the steam turbine rotor and the exposure to fatigue due to thermal stresses. The methodology development is sought to become as general as possible to fit diferent steam turbines, even though the methodology will be tested using process data for a specific steam turbine along with wide assumptions of other necessary data. Other, eventually important and impacting methodology data, such as plant dynamic performance, plant size, dependable equipment, eficiency increasing processes, market conditions, production disturbances and precise design parameters are not extensively considered.

Further, the focus on the rotor as a component is based on literature review findings, and will not rely on any project-performed root cause analysis or failure mode efect analysis among other critical component analysis tools, as the project is limited in the availability of time and access to steam turbine equipment.

## 1.4 Specification of problem

A closer specification of the issue under investigation is summarized as follows:

• Identify previous work and related concepts that have connected maintenance with operational patterns on steam turbines.

• Create a rotor model that is considering temperature diferences in the rotor, relating it to thermal stresses and lifetime, eventually acting as input to maintenance cost calculations.

• Gather qualitative input from the industry to achieve a confirmation on proper methodology development and results.

• Establish scenarios for which maintenance approaches and the relationship between maintenance and operational patterns may be assessed.

• Perform an assessment of the expected change in maintenance cost for a steam turbine rotor depending on the maintenance approache.

## 1.5 Thesis outline

This thesis is structured in seven chapters including the introduction, and it is suggested to read the chapters in the following order.

• Chapter 2 - Theory includes energy technology and production engineering theory that have been used as fundamental knowledge in the project.

• Chapter 3 - Methodology explains how the project was performed and conducted.

• Chapter 4 - Results presents the most relevant results, that followed after the implementation of the methodology.

• Chapter 5 - Discussion highlights discussions points regarding the choice of method, the results and the overall scope of the thesis.

• Chapter 6 - Conclusion summarizes the most important and interesting conclusions.

• Chapter 7 - Future work presents selected suggested starting-points in terms of future work on the topic.

# Theory on Production and Energy Systems

This chapter on production and energy systems is a theoretical framework covering the most essential theoretical parts of the thesis, which seeks to provide enough background for understanding the thesis contents without a previous expertise knowledge.

Considering a production system, it is a concept involving all the relations and interactions between diferent actors and components in a system with a purpose to produce an output [8]. Hence, the general function of a production system can be described as a transformation process of input to output and could be the creating of goods and/or services. With this definition, a production system could be an energy system, that would describe the relations between production, distribution and usage of energy. Further, energy production is typically categorized as a process production. This means that the input is undergoing a physical-chemical process transformed to output, that is hard to restore back into its original raw material.

An overall goal in production systems is often to achieve as high production eficiency and performance as possible. The performance is then often measured by the help of key performance indicators (KPIs). In order for the production system to function properly over time and sustain high eficiency and performance, the system must undergo technical and administrative actions, known as the concept of maintenance [8].

Maintenance has for a long time been seen as a necessary evil in production systems but has evolved to be regarded as a strategic concern [7]. Maintenance can also be considered in a life-cycle perspective stretching from initial planning of the system to its phase-out [8]. By considering maintenance as a strategic element it is possible to accomplish business objectives and with maintenance as a core in the production, it is possible to increase the availability of the resources and produce more when required. As production systems themselves have developed over time and become more advanced and technology-intensive, so has the maintenance management approach followed as well, where the maintenance manager could be confronted with highly technical and demanding questions.

The industrialized world as know today, is currently on the edge of facing a fourth industrial revolution within production, in the industry referred to as the concept of "Industry 4.0". This concept is emphasizing digital technology and built upon advanced computer science, information and communication technology [20]. Big amounts of data are expected to be constantly gathered from the production system and analyzed by artificial intelligence resulting in suggested conclusions. An example of this could be computed conclusions predicting suitable opportunities for carrying out preventive maintenance before a component or system fails.

As an energy system is a concept for all interacting parts in a cycling system related to energy, including production, distribution and usage of the energy, some parts are essential to be explained to understand their relationships. The following sections are explaining those parts that are afiliated with the content of the thesis and eventually followed by explanations on typical production concepts that also are present in energy systems. The following theory sections are starting on higher system-levels and are sequentially being narrowed towards more specific and detailed topics.

## 2.1 Electrical grid

The electrical grid is the physical network that allows the distribution of electricity from producers to consumers. From the power generating plants, transmission lines are carrying high-voltage electricity and is eventually being step-down in voltage and distributed to consumers by local network lines. As electricity is dificult to store in large amounts to a reasonable cost with current technology, the production of electricity must constantly meet the demand. If not, there is a risk of a power outage. The production versus demand is being controlled by monitoring the frequency of the grid. If the consumption is lower than production, the frequency increases, and if consumption is higher than production the frequency decreases [21]. Balancing control is hence an important function in a modern energy system and is commonly a dedicated task to a special control center, known as balance responsibility [22]. This could be related to a strict production chase strategy known from supply and operations planning [4].

With diferent types of power generating plants connected to the grid, the sources are sometimes divided into the dispatchable and the non-dispatchable generation of power sources. The dispatchable generation refers to the type of plants for which its production is possible to start and stop whenever wanted, for example nuclear, thermal and large hydro-electric dams. Wind and solar power are referred to as the non-dispatchable generation since their primary energy sources are varying in availability due to the impact of weather conditions. Their power production is only available based on wind and sun light.

## 2.2 Electricity market

The electricity market refers to the market that is constituting the relations of the actors involved in the energy system focusing on trading electricity. These involved actors are in general producers, distributors and consumers [2], all connected on the grid. It is also common that there is more than one actor-type on the market, for instance, several producers. This is allowing competition. And as the market is determined by the geographical constraints, it is also possible to let the competition stretch over national borders [23]. Also, if major maintenance actions are needed in the system of certain plants, the market and the balance responsible authorities can still manage the production and distribution by creating new running strategies for the other power plants on the grid.

The varying demand and production on the grid are what is contributing to a varying electricity price and fuel costs on deregulated markets. Depending on how the market is divided, there could be varying prices across a geographical area. In Nordic countries, electricity is traded on a common market platform and actors are allowed to buy and sell electricity across national borders [24]. Producers are often closing their selling price 24-hours ahead of production, while consumers are paying a volatile tarif or a fixed price per consumed unit of electricity.

By the increasing availability and possibility of eficient power generation of renewable energy, such as wind and solar energy, the electricity market is evolving. One distinct diference, as distributed generation is becoming encouraged, is the difusing line between producer and consumer [2]. As private home-owners with solar panels or wind generators get the possibility of selling redundant electricity to the market, they become producers. In the case of non-beneficial weather, the home-owner could instead act as a consumer by buying electricity from the market for private usage. This is not only requiring development of the whole energy system but also contributes to the need of reliable and quick responding dispatchable power generation plants that can handle these varying demand patterns.

## 2.3 Electrical power demand and load types

The production of electricity is often measured in watts, while the individual consumption of electricity is measured by watt-hours, often expressed with a prefix. The electricity demand is in general classified in load types related to consumer usage patterns. Two commonly known loads types are base load and peak load.

![](images/c8142bb9dcd9fbc3e0ca67b9a39acbdafc3e5fbed51f92cc03d61c5a38d72158.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/c8142bb9dcd9fbc3e0ca67b9a39acbdafc3e5fbed51f92cc03d61c5a38d72158.jpg

    ```json
{
  "equipment_names": ["Total demand", "Net load", "Solar", "Wind"],
  "equipment_tags_and_identifiers": {
    "Total demand": "- - -",
    "Net load": "orange line",
    "Solar": "dotted yellow line",
    "Wind": "blue dotted line"
  },
  "electrical_components": ["Load [GW]"],
  "mechanical_components": [],
  "connections_between_components": {},
  "flow_direction": {
    "Total demand": "upward trend from 12 AM to 6 PM, then downward",
    "Net load": "initially decreasing, then increasing sharply around 6 PM and leveling off",
    "Solar": "increasing until noon, then decreasing in the evening",
    "Wind": "decreasing throughout the day"
  },
  "numerical_values": {
    "Load [GW]": range(0 to 35)
  },
  "units": ["GW"],
  "labels_and_annotations": {
    "Peak load": "highest point on Net load curve around 6 PM",
    "Base load": "lowest point on Net load curve"
  }
}
```
      
Figure 2.1: Schematic illustration of a total demand curve, base load, peak load and net load, based on Denholm et al. [25].

Figure 2.1 presents the relation of base and peak load, where base load is referring to the electricity usage being the minimum load demanded by society. A good example of this is a night-time where most people are asleep and only essential electrical appliances are turned on. This type of production is often covered by the kind of power plants that do not change their output quickly, for example, nuclear plants and large coal plants. Suddenly, a big increase could appear in the demand but eventually soon diminishes, which is a peak load. An example of this could be the simultaneous usage of microwave-ovens in half-time breaks during major national sports games on television. These loads could typically be covered by the dispatchable generation that can respond quickly to increased demand. The load types are therefore sometimes related to social patterns in society.

As the electrical grid could be connected with wind and solar power generation, this is also introducing net load, also present in Figure 2.1. This type of load is defined as the total power demand minus wind and solar power generation [26]. In such systems, the net load must be covered by the help of dispatchable energy sources that can respond quickly to the demand.

Some power plants have historically been used for base load operations but are likely to face more cyclic operations due to more frequent peaks in the net load. Figure 2.1 shows how decreasing solar production combined with increased demand during the evening creates a ramping need of production that can be solved with flexible dispatchable power generation. This will in many cases fall upon power plants already in use, with configurations that can be ramped, for example, steam turbines. Figure 2.1 may be an extreme case scenario, but it could be close to reality in the near future for developed countries with a high development towards renewable energy production [25]. This requires the systems to be reliable and available when needed, emphasizing the need for proper maintenance.

## 2.4 Maintenance classification

![](images/c0c5d0b9439110c50c3d86aea65eab77d854eeab2d3e9f4a6ca2bc066efde388.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/c0c5d0b9439110c50c3d86aea65eab77d854eeab2d3e9f4a6ca2bc066efde388.jpg

    ```plaintext
- **Equipment names**: None visible in the image.
- **Equipment tags and identifiers**: None visible in the image.
- **Electrical components**: None visible in the image.
- **Mechanical components**: None visible in the image.
- **Connections between components**: None visible in the image.
- **Flow direction**: The flow is from "Business strategy" to "Maintenance strategy," then branching into concepts, policies, and actions. The direction of flow within each level (concepts, policies, actions) is not explicitly shown but can be inferred as downward.
- **Numerical values**: None visible in the image.
- **Units**: None visible in the image.
- **Warning limits**: None visible in the image.
- **Operating limits**: None visible in the image.
- **Labels and annotations**:
  - "Business strategy"
  - "Maintenance strategy"
  - "General decision structure with a set of policies and actions 'The logic and recipe'"
  - "The triggering mechanism for the actions with a set of rules 'How the actions are triggered'"
  - "The actual task to carry out or Intervention with the machine 'What to do?'"
- **Maintenance information**: None visible in the image.
- **Operational information**: None visible in the image.

```
      
Figure 2.2: Hierarchical maintenance levels, based on Pintelon [7].

The previously explained electrical grid and power plants, eventually all require some kind of maintenance over time, either physically or more abstractly with software updates or changes. The view on maintenance as well as its importance difer from case to case, but must certainly be considered in a producing system. Large companies often develop an overall business strategy defining their short and long term goals and a road path for their operations. If the company is a goods-producing company, the business strategy is often followed by a manufacturing strategy defining production related questions. And occasionally, there could also be a defined approach on maintenance included in the manufacturing strategy, here referred to as the maintenance strategy.

Diferent terminology is often used in industry when considering maintenance issues. The following classification of three hierarchical maintenance levels is based on Pintelon [7]. The three considered maintenance levels are the terms concept, policy and action where their relation to each other is illustrated in Figure 2.2.

## 2.4.1 Maintenance concepts

A maintenance concept refers to a set of maintenance policies and actions on lower operational levels and creates the general structure and logic planning of maintenance [7]. In other words, a concept is a recipe or model on the holistic of view on maintenance. In research aiming at reviewing and categorizing maintenance concepts, 24 concepts were identified [27]. As it was concluded that some of them tended to present slightly similar things but in their own approach, it could make it hard to decide suitable maintenance concepts for a particular businesses. With certain prerequisites and requirements, some companies also define their own concepts [7]. Some of the most well-known concepts are life-cycle costing (LCC), total productive maintenance and reliability-centered maintenance.

## 2.4.2 Maintenance policies

A maintenance policy is a set of rules that determine the triggering mechanisms for maintenance actions [7]. Table 2.1 is presenting four maintenance policies, which each are triggering maintenance actions.

Table 2.1: Description of four maintenance policies [7].
<table><tr><td>Policy</td><td>Description</td></tr><tr><td>FBM</td><td>Failure-based maintenance A policy that is triggering maintenance actions once a failure or break- down has occurred.</td></tr><tr><td>TBM</td><td>Time-based maintenance Maintenance actions are triggered based on a set time or usage inter- val, for instance hours. The triggered actions aim at preventing failure to occur.</td></tr><tr><td>CBM</td><td>Condition-based maintenance Suitable system parameters are being monitored, such as vibrations, oil viscosity, temperatures, pressures, flow rates, acoustics etc. and are compared with predetermined values. If the measured parameter is exceeding the set limit, typically lower than the limit of failure, a</td></tr><tr><td>OBM</td><td>preventive maintenance action is triggered. Opportunity-based maintenance Maintenance actions are carried out once an opportunity arises. This is a typical policy to apply on non-critical or long-life components. Or in cases where it is simply not possible to interact with the component without extensive work. These opportunities can though arise non- periodically.</td></tr></table>

## 2.4.3 Maintenance actions

A maintenance action is the actual maintenance intervention or elementary task that is being carried out by a technician on a particular component or machine. The action can be defined as either a corrective action or a precautionary action [7]. A corrective action is an activity repairing or restoring an item back to a functioning condition and occurs after the item has failed or has broken down. A precautionary action is an activity that has a goal of diminish or avoid a possible failure to occur. It is assumed that precautionary actions are cheaper than corrective ones [7].

## 2.5 Maintenance as a service

As the view on maintenance has evolved over time, maintenance activities have gradually been integrated into product-service system (PSS) solutions [28]. It is now not uncommon that customers are not only ofered a product but instead a function where maintenance often is included. Examples of PSS-solutions are station-based car-sharing services, city rental bikes and jet engines powered-by-the-hour. Several of these solutions enable remote maintenance monitoring with data-driven maintenance approaches in order to make sure its function can be provided. This product-service system is also appearing in the power generation industry [29]. Three types of service approaches are hereby introduced. These are internal crew, external service and external service with a framework contract.

## 2.5.1 Internal crew

Maintenance by an internal crew is defined as maintenance that is being performed by internal employees of the machine user [30]. They generally have their own facili ties on-site and an internal system for receiving, prioritizing and planning upcoming work.

## 2.5.2 External service

External service is maintenance carried out by an external service company, that will perform maintenance upon the customer’s request [30]. The external maintenance company typically have their facilities located on a remote location and apply a rate when service is performed.

## 2.5.3 External service with framework contract

External service with a framework contract refers to maintenance carried out by an external company that has written a contract with the customer on how and when maintenance will be performed [30]. This type of contract can entail either a fixed or varying cost. This type of external service is sometimes provided by the original equipment manufacturer (OEM) and could then be providing up-time or power-by hour service [28]. This could also allow the OEM to gather data on how their machines are operated and use the data for future research and development. Another approach from the OEM could be to only sell their products using this PSS-approach. External service based on framework contracts is common in the turbine industry [31]–[33].

## 2.6 Dependability

![](images/334d612016edbbd9407c9a18e63cf14a7ca41b26b3be1bc41add4f9b31924089.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/334d612016edbbd9407c9a18e63cf14a7ca41b26b3be1bc41add4f9b31924089.jpg

    ```plaintext
Equipment names:
- Reliability
- Maintainability
- Maintenance support

Equipment tags and identifiers: None visible in the image.

Electrical components: None visible in the image.

Mechanical components: None visible in the image.

Connections between components:
- Reliability is connected to Dependability.
- Maintainability is connected to Dependability.
- Maintenance support is connected to Dependability.

Flow direction: The flow direction is not explicitly shown, but it can be inferred that all connections lead from their respective components (Reliability, Maintainability, and Maintenance support) towards Dependability.

Numerical values: None visible in the image.

Units: None visible in the image.

Warning limits: None visible in the image.

Operating limits: None visible in the image.

Labels and annotations:
- Reliability
- Maintainability
- Maintenance support
- Dependability

Maintenance information: None visible in the image.

Operational information: The diagram illustrates a hierarchical relationship where reliability, maintainability, and maintenance support are sub-components of dependability. This suggests that for an industrial system to be dependable, it must have reliable components, be easily maintained, and receive adequate maintenance support.
```
      
Figure 2.3: Factors afecting the dependability of the system, adapted from Bellgran and Safsten [8].

The term dependability intends to describe a system’s ability to perform when required [34] and considering production systems, dependability is often including the concepts of reliability, maintainability and maintenance support [8]. The relation of them is illustrated in Figure 2.3 for which explanations follow.

## 2.6.1 Reliability

Reliability is a system’s ability to perform as required without the occurrences of failure, under given conditions and time intervals and is measured as the probability of survival at a specific point of time, noted as R(t) [34]. The given conditions refer to aspects that could impact on the reliability, for example, operation mode, stress level, temperature, pressure and previous maintenance actions. What is being considered as the system is defined by the user and could be a machine itself, a sub-system of the machine or just one component in the machine.

The reliability of an item generally follows a certain underlying statistical distribution, where common distributions are exponential, log-normal and Weibull distributions. For mechanical components exposed to fatigue, the Weibull distribution is generally known as a suitable lifetime distribution [30], with the two-parameter probability density function (pdf):

$$
f ( t ) = \frac { \beta } { \eta } \left( \frac { t } { \eta } \right) ^ { \beta - 1 } e ^ { - \left( \frac { t } { \eta } \right) ^ { \beta } }\tag{2.1}
$$

where: t = Specified period of time

β = Shape parameter of the distribution, also known as the slope

η = Scale parameter of the distribution, also known as the characteristic life

Equation (2.2) is describing how to calculate reliability using a two-parameter Weibull distribution. Depending on the parameter values of the Weibull distribution, diferent life behaviours can be described [30].

$$
R ( t ) = e ^ { - \left( \frac { t } { \eta } \right) ^ { \beta } }\tag{2.2}
$$

If integrating the reliability from 0 to $\infty$ , it is possible to obtain the Mean Time To Failure (MTTF), a common maintenance KPI, stating the average time between consecutive failures.

$$
\mathrm { M T T F } = \int _ { 0 } ^ { \infty } R ( t ) \ \mathrm { d } t\tag{2.3}
$$

## 2.6.2 Maintainability

The maintainability of a system refers to the ability of an item to be restored to its operational function within a given period of time and given conditions [30]. The given conditions in terms of maintainability include accessibility of the component, needed maintenance procedures and necessary maintenance resources [34].

A common KPI afiliated with maintainability is the Mean Time To Repair (MTTR), which is a measure stating the average time it takes to restore a failed item. The measure is closely related to MTTF and the availability A, of a considered system, where the availability is defined as an item’s ability to be in a performing state when required [34]. Equation (2.4) describes how the availability of a system can be calculated based on known values of MTTF and MTTR.

$$
A = { \frac { \mathrm { M T T F } } { \mathrm { M T T F } + \mathrm { M T T R } } }\tag{2.4}
$$

## 2.6.3 Maintenance support

Maintenance support is the providing of resources such as labour, equipment, materials, spare parts, facilities and instructions that are needed in order to maintain an item [34]. The maintenance support concerns questions that are closely related to the type of chosen maintenance service.

## 2.7 Power generation by steam turbines

The electrical grid can be provided with electricity by the help of various kinds of power generation plants as described in section 2.1. An example of such plants are thermal power plants using steam turbines for converting the thermal energy into electricity.

![](images/cfcae2e117161338254f3fd4045ad1dd92a30b44bafbc88684f8452bf0ba45f9.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/cfcae2e117161338254f3fd4045ad1dd92a30b44bafbc88684f8452bf0ba45f9.jpg

    1. Equipment names:
   - Steam generator
   - Steam turbine
   - Generator (G)
   - Condenser

2. Equipment tags and identifiers:
   - Fuel → to steam generator
   - Steam → from steam generator to steam turbine
   - Water → from condenser back to steam generator

3. Electrical components:
   - None visible in the image.

4. Mechanical components:
   - Steam generator (cylinder with heating elements)
   - Steam turbine (cone-shaped component)
   - Condenser (box-like component)

5. Connections between components:
   - Fuel → Steam generator
   - Steam → Steam turbine
   - Water → Condenser

6. Flow direction:
   - Fuel flows into the steam generator.
   - Steam is generated and flows to the steam turbine.
   - Water returns from the condenser back to the steam generator.

7. Numerical values:
   - None visible in the image.

8. Units:
   - None specified for numerical values or units.

9. Warning limits:
   - None specified.

10. Operating limits:
    - None specified.

11. Labels and annotations:
    - Steam generator
    - Fuel → to steam generator
    - Steam → from steam generator to steam turbine
    - Water → from condenser back to steam generator

12. Maintenance information:
    - None visible in the image.

13. Operational information:
    - The diagram represents a thermal power plant process where fuel is used to heat water, generating steam which drives a steam turbine connected to an electrical generator.
    - The steam then cools and condenses back into water, which is recycled through the system.
      
Figure 2.4: A basic schematic illustration of a steam cycle.

Figure 2.4 illustrates a basic steam cycle producing electricity. Starting with a suitably selected fuel for the specific power plant, the fuel is combusted and starts to heat up water-filled pipes lead through the steam generator. After the steam leaves the steam generator it is being delivered, highly pressurized, to the steam turbine. The steam expands in the the steam turbine and converts thermal energy to mechanical energy by flowing through its turbine blades making the rotor spin, generating electricity by the help of the connected power generator [35]. With the turbine blades placed in a sequence of diferent sizes, it is referred to as the number of stages.

After the steam turbine, the steam condensates back to water. In order to increase the eficiency of the plant, condensation could be made by heating water used in a district heating system. This makes the plant a so called combined heat and power plant. Lastly, the water is pumped back to the steam generator, repeating the principle of the steam cycle.

## 2.7.1 Steam turbine fundamentals

A steam turbine allows conversion of thermal energy to mechanical energy due to the enthalpy of the steam. When modelling a steam turbine for computational calculations, it is possible to calculate the enthalpy after the turbine module using the enthalpy before the turbine, the machine eficiency and the nominal values [36]. The mechanical power produced by the turbine can then be computed and transferred

to a power generator model.

The steam turbine model may describe the turbine either with a single turbine section or with many sections in order to consider the steam extractions, which is done for increased eficiency of the cycle. The pressure change is however defined as a function of the nominal mass flow rate, the nominal pressure at the turbine inlet and the nominal pressure at the turbine outlet [36].

$$
\dot { m } = \dot { m } _ { n o m } \frac { p _ { i n t } } { p _ { i n t , n o m } } \sqrt { \frac { 1 - \left( \frac { p _ { o u t } } { p _ { i n l } } \right) ^ { \frac { n + 1 } { n } } } { 1 - \left( \frac { p _ { o u t , n o m } } { p _ { i n l , n o m } } \right) ^ { \frac { n + 1 } { n } } } }\tag{2.5}
$$

with:

$$
n = \frac { \ln { \frac { p _ { o u t } } { p _ { i n l } } } } { \ln \left( { \frac { p _ { o u t } } { p _ { i n l } } } \right) - \ln \left( { \frac { T _ { o u t } } { T _ { i n l } } } \right) }\tag{2.6}
$$

where: m˙ = Mass flow rate [kg/s]

$$
\dot { m } _ { n o m } = \mathrm { N o m i n a l ~ m a s s ~ f l o w ~ r a t e ~ [ k g / s ] }
$$

$$
\begin{array} { r l } { p _ { i n l } } & { { } = \mathrm { P r e s s u r e ~ a t ~ i n l e t ~ [ P a ] } } \end{array}
$$

$$
\begin{array} { r l } { p _ { o u t } } & { { } = \mathrm { { P r e s s u r e ~ a t ~ o u t l e t } ~ [ P a ] } } \end{array}
$$

$$
\begin{array} { r l } { T _ { i n l } } & { { } = \mathrm { T e m p e r a t u r e \ a t \ i n l e t \ [ K ] } } \end{array}
$$

$$
\begin{array} { r l } { T _ { o u t } } & { = \mathrm { T e m p e r a t u r e \ a t \ o u t l e t { \ [ K ] } } } \end{array}
$$

The steam turbine expansion is not totally isentropic nor isothermal and is therefore dependent on the isentropic eficency. The eficiency is generally assumed to be constant for every section of the turbine due to simplicity. Isentropic eficiency of a steam turbine is defined as [36]:

$$
\eta _ { T } = \frac { R e a l \ t u r b i n e \ w o r k } { I s e n t r o p i c \ t u r b i n e \ w o r k } = \frac { \Delta h _ { t u r b } } { \Delta h _ { i s } } = \frac { h _ { i n } - h _ { o u t } } { h _ { i n } - h _ { o u t , i s } }\tag{2.7}
$$

The isentropic enthalpy at the outlet can further be described as a function of the pressure. The shaft work for a section is therefore:

$$
\Delta h _ { t u r b } = \eta _ { T } \left( h _ { i n } - h _ { o u t , i s } \right)\tag{2.8}
$$

And the total power output for a turbine with k number of sections is:

$$
P _ { e l } = \sum _ { i = 1 } ^ { i = k } \Delta h _ { t u r b , i } \dot { m _ { i } }\tag{2.9}
$$

## Transient heat transfer

The Dittus-Boetler Equation (2.10) for turbulent pipe flow can be used as an approximation to calculate the the Nusselt number (Nu) inside a steam turbine as a function of the Reynolds number (Re), Prandtl numer (Pr) and a correction factor K. These are then used to calculate the convective heat transfer coeficient (HTC) [13].

$$
N u = K \cdot R e ^ { 0 . 8 } \cdot P r ^ { 0 . 3 3 3 }\tag{2.10}
$$

The HTC governs the temperature profile in the boundary layer between steam flow and rotor surface. Since a steam turbine has a complex geometry, the Reynolds number would be dificult to determine. Instead, the HTC can be expressed as a function of HTC at nominal load [37], see Equation (2.11) . The equation is based on the proportionality of the HTC in relation to the Reynolds number, which in turn makes the proportional to the mass flow rate, $\dot { m } ^ { 0 . 8 }$

$$
\frac { H T C } { H T C _ { n o m } } = \left( \frac { \dot { m } } { \dot { m } _ { n o m } } \right) ^ { 0 . 8 }\tag{2.11}
$$

HTC is one of the most critical variables in the calculations for transient conduction. The calculation for radial temperature gradient in the rotor is solved by discretizing the temperature into small time steps and introducing the non-dimensionalizing of the governing equations [38]. The temperature diference between the rotor and steam flow, θ, is divided by the maximum possible temperature diference $\theta _ { i }$

$$
\theta ^ { * } = \frac { \theta } { \theta _ { i } } = \frac { T - T _ { \infty } } { T _ { m } - T _ { \infty } }\tag{2.12}
$$

$$
\begin{array} { r } { \mathrm { ~ w h e r e : ~ } T _ { \infty } = \mathrm { S t e a m ~ t e m p e r a t u r e ~ } [ ^ { \circ } \mathrm { C } ] \qquad } \\ { T _ { m } = \mathrm { I n i t i a l ~ m e t a l ~ t e m p e r a t u r e ~ } [ ^ { \circ } \mathrm { C } ] } \end{array}
$$

The purpose of non-dimensionalizing the temperature diference is to express $\theta ^ { * }$ as a function of dimensionless numbers. These numbers are a spatial dimensionless coordinate, a dimensionless time and the ratio of thermal resistance [39].

By definition $\theta ^ { * }$ must be in the range $0 < \theta ^ { * } < 1$ . A spatial dimensionless coordinate using the radius of a rotor, $r _ { 0 } ,$ is defined as:

$$
r ^ { * } = \frac { r } { r _ { 0 } }\tag{2.13}
$$

The dimensionless time is also known as the Fourier number (Fo), which is defined as:

$$
F o = \frac { \alpha _ { d i f f } \cdot t } { { r _ { 0 } } ^ { 2 } }\tag{2.14}
$$

where $\alpha$ is the thermal difusivity of the rotor material, which combines thermal conductivity with density and heat capacity:

$$
\alpha _ { d i f f } = \frac { \lambda } { C _ { p } \cdot \rho }\tag{2.15}
$$

The ratio of thermal resistance, or the Biot number (Bi), compares the convective heat transfer calculated in Equation (2.11) to the heat transfer within the body [38].

$$
B i = { \frac { r _ { 0 } \cdot H T C } { \lambda } }\tag{2.16}
$$

where λ is the thermal conductivity of the rotor material.

The exact solution for $\theta ^ { * }$ can then be expressed as a function of $r ^ { * }$ , Bi and Fo [39].

$$
\theta ^ { * } = f ( r ^ { * } , B i , F o ) = \sum _ { n = 1 } ^ { \infty } C _ { n } \cdot e ^ { \left( - \zeta _ { n } ^ { 2 } F o \right) } \cdot J _ { 0 } \left( \zeta _ { n } r ^ { * } \right)\tag{2.17}
$$

The Biot number is used to determine $\zeta _ { n }$ and $C _ { n }$ which are roots to the Bessel function $J _ { 0 }$ . The first roots as functions of the Biot number are presented in Table 2.2. By solving Equation (2.17), the temperature gradient can be found at any radial position in the component.

Table 2.2: Shortened table with coeficients for the one-term approximation to the series solution for transient conduction, based on Özisik [38].
<table><tr><td>Bi</td><td> $\zeta _ { 1 }$   $C _ { 1 }$ </td></tr><tr><td>0.01 0.1412</td><td>1.0025</td></tr><tr><td>0.04</td><td>0.2814 1.0099</td></tr><tr><td>0.08</td><td>0.3960 1.0197</td></tr><tr><td>0.10</td><td>0.4417 1.0246</td></tr><tr><td>0.30</td><td>0.7465 1.0712</td></tr><tr><td>0.70</td><td>1.0873 1.1539</td></tr><tr><td>1 1.2558</td><td>1.2071</td></tr></table>

## Start-up types and its conditions

When starting a steam turbine, there are typically three types of start-up scenarios to consider; cold, warm and hot start-ups. Which type of start-up that is being initiated, is generally defined by the turbine casing metal temperature measured at the steam turbine just before the start-up begins.

By considering the rotor in the steam turbine, the type of start-up can be determined by the temperature diference between the rotor surface and the rotor mean temperature, see Equation (2.18). The temperature diferences further act as input to the calculations of thermal stresses, see Equation (2.19).

$$
\Delta T = T _ { S } - { \overline { { T } } } = T _ { S } - { \frac { 2 } { { r _ { 0 } } ^ { 2 } } } \cdot \int _ { 0 } ^ { r _ { 0 } } r \cdot T ( r ) \ d r\tag{2.18}
$$

where: $r _ { 0 }$ = Rotor radius [m]

r = Radial coordinate [m]

$T$ = Temperature at the radial coordinate location [°C]

$T _ { S }$ = Rotor surface temperature $\big [ \mathrm { } ^ { \circ } \mathrm { C } \big ]$

$\overline { T }$ = Mean rotor temperature $\mathrm { [ ^ { \circ } C ] }$

## Thermal stresses due to start-ups

Starting up a turbine too quickly will most likely result in failures due to low-cycle fatigue and thermal expansions. If wanted to reduce the risk of fatigue, the start-up time must be limited with respect to thermal stresses [40]. A thermal stress module is generally a part of the turbine control system, which is continuously evaluating and monitoring the thermal stress at critical locations and helps to limit the temperatures. These critical locations are often those with the largest wall thickness causing the largest thermal diferences [12]. The thermal expansions can further cause glitches in the turbine, leading to vibrations and uneven spinning. In a worstcase scenario, a blade can loosen and penetrate through the casing.

The rotor in the steam turbine can be approximated as a solid cylinder of infinite length [41], being heated on the surface, the permissible stress can be calculated by using Equation (2.19), where $k _ { c }$ is a stress concentration factor taking actual geometrical change of the rotor in consideration [16] and the axial stress, $\sigma _ { z } .$ is assumed to be the same as the hoop stress.

$$
\sigma _ { z } = k _ { c } \cdot \frac { E \cdot \alpha _ { e x p } \cdot \Delta T } { 1 - \nu }\tag{2.19}
$$

where: $\sigma _ { z }$ = Axial stress [Pa]

$k _ { c }$ = Stress concentration factor

$E$ = Young’s modulus for given material $\mathrm { [ P a ] }$

$\alpha _ { e x p }$ = Coeficient of thermal expansion $\big [ \mathrm { } ^ { \circ } \mathrm { C } ^ { - 1 } \big ]$

$\Delta T$ = Rotor temperature diference $\big [ \mathrm { } ^ { \circ } \mathrm { C } \big ]$

$$
\begin{array} { r l } { \nu } & { { } = \mathrm { P o i s s o n ' s ~ r a t i o ~ } \big [ - \big ] } \end{array}
$$

Based on the calculated maximum stress of each start-up type, the number of cycles to failure on the specific stress level can be obtained. This is typically done by the help of an S-N curve for the specific component material that is stating the correlation between stress level and its number of cycles to failure.

## Equivalent operating hours

Depending of the type of start-up, the start types require diferent ramping times in order to reach the full power output of the steam turbine without exceeding the permissible thermal stress levels. This means that a cold start, requiring a long start-up time and causes higher stress levels than a hot start, will tear more on the turbine. Equivalent operating hours (EOH) is then introduced as a concept that supports lifetime calculations of components exposed to thermal stress by translating operating hours on various stress levels to an equal and comparable amount of time in relation to how they wear the turbine.

In order to calculate a total number of EOH, individual EOH-numbers for each startup type are required. Further, the expected lifespan $\tau _ { l i f e }$ of the rotor is required as input to those calculations, beneficially based on the manufacturer’s specifications. From Aminov et al. [18] the total EOH is described as:

$$
E O H = \sum _ { i = 1 } ^ { k } a _ { i } n _ { i } + \sum _ { j = 1 } ^ { y } b _ { j } \psi _ { j }\tag{2.20}
$$

where $k$ is the number of start-up types, $a _ { i }$ is the time coeficient of EOH for the i-th start type and $n _ { i }$ is the scenario input on the number of start-up types. The second summation part of Equation (2.20) is considering load changes where $y$ is the number of operating regimes, $b _ { i }$ is a coeficient for the operating regime of the j-th load and $\psi _ { j }$ is the time in operation for the j-th load [18].

As the start-up types are causing various damage to the rotor due to their stress amplitudes, it is of interest to introduce a cumulative damage model. A commonly known model is the Palmgren’s-Miners’ rule for fatigue damage in combination with Robinson’s hypothesis considering creep [12], see Equation (2.21). When the damageability parameter $Z$ is reaching 1, failure commonly occurs, but it should be denoted that failure mechanisms can appear earlier than $Z = 1$ . In Equation (2.21), the Palmgren’s-Miners’ rule is denoted by $Z _ { F }$ and Robinson’s by $Z _ { C }$

$$
Z = Z _ { F } + Z _ { C } = \sum _ { i = 1 } ^ { k } { \frac { n _ { i } } { N _ { i } } } + \sum _ { j = 1 } ^ { r } { \frac { t _ { j } } { t _ { B j } } }\tag{2.21}
$$

where $N _ { i }$ is the number of cycles to failure for the i-th start type, $t _ { j }$ is the time of a load at a given temperature and magnitude and $t _ { B j }$ is the time to rupture at the j-th load [12]. As the thesis is only focusing on fatigue caused by thermal stresses from start-ups, the aspects of load changes and creep, $b _ { i }$ and $Z _ { C }$ will not further be explained, but are important to keep in mind. From Equation (2.20) we recall the time coeficient $a _ { i } ,$ defined by Aminov et al. [18] as:

$$
a _ { i } = \frac { \tau _ { l i f e } } { Z } \cdot \frac { 1 } { N _ { i } }\tag{2.22}
$$

Lastly, the total EOH can be divided by the expected years in service Y and give the number of EOH on a yearly basis.

## 2.7.2 Maintenance on steam turbines

A steam turbine consists of some major components that are crucial for the turbine functioning and are supported by sub-systems allowing the turbine to actually work. Examples of major components are the rotating discs equipped with blades, the shafts, the rotor, bearings, seals and casings [42]. These components are in general exposed to several possible failure mechanisms such as corrosion, creep, fatigue and stress cracking. As failures typically occur on diferent components, it is often suitable to apply separate strategies for maintenance depending on the type of machine part. From the OEM, the turbine is often stated to be monitored based on some specific measures such as the speed, load, pressures, temperatures and possibly also vibrations and expansions [42]. And it is common nowadays that the OEM is ofering full maintenance programs for certain components or even the whole plant by signing service contracts [32], [33], [43].

Maintenance on steam turbines is typically carried out based on inspection intervals with frequencies varying from daily, weekly, monthly and annually intervals. Commonly spoken outages, where the steam turbine is stopped for a time and inspection, reparation and replacements are taking place, are known as minor and major outages occurring every 3-5 years and 9-12 years respectively or every 25 000 EOH and 100 000 EOH respectively [42].

A minor inspection on the steam turbine is a periodic inspection, related to the maintenance policy TBM, due to its occurrence every 25 000 EOH. During this outage, the turbine casing, bearing pedestals and generator remain closed, while inspection is performed, on for example, the control system, control valves and the turbo-set [41]. It is also possible to include boroscopic inspections and diagnostic measurements. A minor inspection could typically require 2-7 days to perform.

A major outage is a more extensive TBM-approach and an inspection occurring every 100 000 EOH, often requiring 40-60 days of outage [41]. During this inspection, basically all components and systems are inspected visually, diagnostically or by testing. Casings are opened up and worn out parts are repaired or replaced, and tolerances are checked. Imperfections are reviewed and the aim is to restore the steam turbine back to perfect shape. These operations often require a large group of personnel where it is not unusual that a representative from the OEM is present during the maintenance operation and restoration [32], [41].

## 2.8 Cost calculations on maintenance

Maintenance can be evaluated and calculated by using various approaches and perspectives, typically based on the chosen maintenance concept approach. One of the presented evaluation models by Lundgren et al. [27] is the Life Cycle Costing analysis (LCC) approach evaluating the impact of maintenance from cradle to grave and can also be designed in such way that it helps to evaluate whether maintenance should be performed using internal or external service [27]. With the increasing demand and requirements on sustainable energy production processes, a cost analysis model spanning over the whole life cycle is a suitable evaluation model. The LCC-analysis could not only help to minimize the cost of maintenance by evaluating strategies but also be adjusted towards a life cycle profit model, that could consider a loss of income due to maintenance issues [27].

Reina et al. [30] present a maintenance planning software with calculations on how to calculate LCC maintenance costs and eventually help to design a maintenance plan based on the minimum cost. The costs are further divided into four types of maintenance policies; failure-based maintenance (FBM), time-based maintenance (TBM), condition-based maintenance (CBM) and opportunity-based maintenance (OBM). Each policy, are then evaluated for both internal, external and external contract maintenance services.

## 2.8.1 Failure-based maintenance

Failure-based maintenance can be calculated by using Equations (2.23)-(2.25) for an internal crew (-INT), external service (-EXT) and external service with framework contract (-FWC) [30]. In the case of considering the rotor on a steam turbine, the use of an FBM-policy would mean that the steam turbine is running until it fails and eventually causes collateral damage. The maintenance department would then act on the breakdown as a trigger and would initiate a reparation or replacement action.

$$
\begin{array} { r } { C _ { F B M _ { I N T } } = \frac { L _ { I N T } } { 1 / \int _ { 0 } ^ { \infty } R ( t ) d t } + C _ { C D } + \sigma _ { S P } \cdot C _ { S P } + F _ { F B M } } \\ { + ( M D T i n t + \sigma _ { S P } \cdot S D T + \mathrm { M T T R } ) \cdot C _ { L P } } \end{array}\tag{2.23}
$$

$$
\begin{array} { r } { C _ { F B M _ { E X T } } = L _ { E X T } \cdot \mathrm { M T T R } + C _ { C D } + \sigma _ { S P } \cdot C _ { S P } + F _ { F B M } } \\ { + ( M D T e x t + \sigma _ { S P } \cdot S D T + \mathrm { M T T R } ) \cdot C _ { L P } } \end{array}\tag{2.24}
$$

$$
\begin{array} { r l } & { C _ { F B M _ { F W C } } = \frac { { { L _ { F W C } } / { O H _ { Y } } } } { { 1 / \int _ { 0 } ^ { \infty } { { R ( t ) d t } } } } + C _ { C D } + \sigma _ { F W C } \cdot C _ { S P } } \\ & { ~ + ( M D T e x t + \mathrm { M T T R } ) \cdot { C _ { L P } } } \end{array}\tag{2.25}
$$

## 2.8.2 Time-based maintenance

Time-based maintenance can be calculated by using Equations (2.26)-(2.28) for the three types of services INT, EXT and FWC [30]. In terms of the steam turbine and its rotor when applying a TBM-policy, it is close to industry practice today [32], [33], [42]. The rotor is then inspected based on a time-based interval which is pre-defined by either the OEM or the user. The actions taken during a TBM-policy approach are preliminary preventive actions where the goal is to maintain the item in a functional condition and diminish the possibilities of failures to even happen.

$$
C _ { T B M _ { I N T } } = \frac { L _ { I N T } } { 1 / E _ { T B M } } + \xi \cdot T M \cdot C _ { L P } + \sigma _ { S P } \cdot C _ { S P } + F _ { T B M }\tag{2.26}
$$

$$
C _ { T B M _ { E X T } } = L _ { E X T } \cdot T M + \xi \cdot T M \cdot C _ { L P } + \sigma _ { S P } \cdot C _ { S P } + F _ { T B M }\tag{2.27}
$$

$$
C _ { T B M _ { F W C } } = \frac { L _ { F W C } / O H _ { Y } } { 1 / E _ { T B M } } + \xi \cdot T M \cdot C _ { L P } + \sigma _ { F W C } \cdot C _ { S P }\tag{2.28}
$$

## 2.8.3 Condition-based maintenance

Condition-based maintenance can be calculated by using Equations (2.29)-(2.31) for INT, EXT and FWC services [30]. When using a CBM-policy on a steam turbine rotor, the machine must be equipped with sensors and other diagnostic tools that can support the gathering of online performance data. The data must then be analyzed, preferably in real time by a computer. By trend analysis and pre-set limits, maintenance actions are triggered. This would mean that the policy could have varying time intervals for which preventive maintenance tasks are carried out. The aim is to predict failures to occur just in time before they happen.

$$
C _ { C B M _ { I N T } } = \frac { L _ { I N T } } { 1 / \mathrm { M T T F } \cdot 0 , 7 5 \cdot p _ { 1 } \cdot ( 1 - p _ { 2 } ) } + T M \cdot C _ { L P } + C _ { S P } + F _ { C B M }\tag{2.29}
$$

$$
C _ { C B M _ { E X T } } = L _ { E X T } \cdot T M + T M \cdot C _ { L P } + C _ { S P } + F _ { C B M }\tag{2.30}
$$

$$
C _ { C B M _ { F W C } } = \frac { L _ { F W C } / O H _ { Y } } { 1 / \mathrm { M T T F } \cdot 0 , 7 5 \cdot p _ { 1 } \cdot ( 1 - p _ { 2 } ) } + T M \cdot C _ { L P } + C _ { S P }\tag{2.31}
$$

## 2.8.4 Opportunity-based maintenance

Opportunity maintenance can be calculated by using Equations (2.32)-(2.34) for the three labour services [30]. The OBM-policy is a suitable approach of maintenance when there are opportunities arising periodically with enough time available for the carrying through of preventive actions. In the steam turbine case, these opportunitywindows could typically appear when the demand from the market is low and it can be covered by other power plants. These time windows could eventually be predicted by using computers.

$$
C _ { O B M _ { I N T } } = \frac { L _ { I N T } } { 1 / t } + T M \cdot C _ { L P } + \sigma _ { S P } \cdot C _ { S P } + F _ { O B M }\tag{2.32}
$$

$$
C _ { O B M _ { E X T } } = L _ { E X T } \cdot T M + T M \cdot C _ { L P } + \sigma _ { S P } \cdot C _ { S P } + F _ { O B M }\tag{2.33}
$$

$$
C _ { O B M _ { F W C } } = \frac { L _ { F W C } / O H _ { Y } } { 1 / t } + T M \cdot C _ { L P } + \sigma _ { F W C } \cdot C _ { S P }\tag{2.34}
$$

## Methodology

The methodology chapter presents the methods that were used in order to achieve the aim of the thesis. The overall work consisted of the development of a methodology that can be used to assess thermal stresses on a steam turbine rotor and its impact on the rotor lifetime, depending on scenarios, which serve as a basis for maintenance cost calculations related to maintenance policies and services. The developed methodology was eventually tested with data and evaluated on how well it manages to achieve the task, for which the methodology chapter presents how that work was executed.

The methodology framework development was structured in three steps, to which the chapter has also been sectioned. The steps were:

1. Development of methodology framework

2. Determination of data input

3. Scenarios and result analysis

Further, interviews were conducted during the thesis with the aim to strengthen hypotheses and calculated results. The interviews were set up semi-structurally, where questions were asked related to the topic and some specific methodology parts, and the respondent was allowed to answer precisely or give a more elaborate answer. The mix of questions and answers did not just only strengthen results but also acted as good input to discussion, conclusion and future work. The respondents were experienced people from the industry with extensive knowledge of steam turbine processes. The questions are retrieved in Appendix A.

## 3.1 Development of methodology framework

![](images/cd27446b203bc7da3be84d5e848da73c7082e09360fd16677bc0adc82b23b12e.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/cd27446b203bc7da3be84d5e848da73c7082e09360fd16677bc0adc82b23b12e.jpg

    ```plaintext
1. Equipment names:
   - Steam turbine simulation
   - EOH (End of Life) and Reliability
   - Maintenance cost calculations
   - Result presentation

2. Equipment tags and identifiers:
   - Scenarios on No. of start-ups
   - Transient simulation
   - Temperature differences
   - Thermal stresses
   - Stress-profiles
   - Cycles to failure
   - Calculation of time coefficients
   - Cost of FBM (Failure-Based Maintenance)
   - Cost of CBM (Condition-Based Maintenance)
   - Cost of OBM (Opportunity-Based Maintenance)
   - Cost of TBM (Time-Based Maintenance)

3. Electrical components:
   None visible.

4. Mechanical components:
   - Steam turbine simulation
   - Stress-profiles

5. Connections between components:
   - Scenarios on No. of start-ups → Transient simulation
   - Transient simulation → Temperature differences
   - Temperature differences → Thermal stresses
   - Thermal stresses → Stress-profiles
   - Stress-profiles → Calculation of R(t), MTTF, MTTR (Reliability)
   - Stress-profiles → Calculation of EOH (End of Life)
   - Cycles to failure → Stress-profiles
   - Calculation of time coefficients → Stress-profiles

6. Flow direction:
   The flow is from left to right and then branches out into different calculations.

7. Numerical values:
   None visible.

8. Units:
   - R(t) (Reliability)
   - MTTF (Mean Time To Failure)
   - MTTR (Mean Time To Repair)
   - EOH (End of Life)

9. Warning limits:
   None visible.

10. Operating limits:
    None visible.

11. Labels and annotations:
    - Scenarios on No. of start-ups
    - Transient simulation
    - Temperature differences
    - Thermal stresses
    - Stress-profiles
    - Cycles to failure
    - Calculation of time coefficients
    - Cost of FBM, CBM, OBM, TBM

12. Maintenance information:
    - Cost calculations for Failure-Based Maintenance (FBM), Condition-Based Maintenance (CBM), Opportunity-Based Maintenance (OBM), and Time-Based Maintenance (TBM)

13. Operational information:
    The diagram outlines a process flow from scenarios on the number of start-ups through transient simulation, temperature differences, thermal stresses, stress-profiles, cycles to failure, and calculation of time coefficients leading into reliability metrics (R(t), MTTF, MTTR) and end-of-life calculations (EOH). Maintenance costs are calculated based on these metrics.
```
      
Figure 3.1: Visual mapping of methodology framework.

Figure 3.1 illustrates the mapping of the methodology, which was developed by splitting it into four parts. These four parts are noted as the bottom elements in Figure 3.1 and are steam turbine simulation, reliability and EOH data, maintenance calculations and result presentation. The complete methodology development took place in a <sup>Matlab</sup>-environment allowing construction of algorithms and mathematical computations. The following sub-sections reflect the four presented elements of the methodology.

The left top part of the figure was the starting point of the methodology, requesting scenario input for the succeeding transient simulations of the steam turbine rotor. From the simulation, the temperature diferences were sought to be obtained for which thermal stresses could be determined. Based on the calculated stress levels, stress-profiles and the maximum number of cycles to failure were given.

When the numbers of cycles to failure and the stress-profiles were defined, calculations on time coeficients allowed calculations of EOH and reliability respectively. The numbers of cycles are input to the LCC-calculations for assessing the FBM-, TBM-, CBM- and OBM-policies for maintenance on a steam turbine rotor. Finally, the cost model normalizes the results and present them in comparable numbers (SEK/MWh).

The construction of Figure 3.1 and the methodology was conducted by performing literature searches on theory as well as studies on industry practice. Covered literature material were printed books, e-books, journal articles, web-pages, video tutorials and grey literature. Grey literature included documents such as conference abstracts, presentations, proceedings, regulatory data, unpublished data, government publications and reports (such as white papers, working papers and internal documentation). Major parts of the literature review were also serving as input for the writing of the theoretical background.

## 3.1.1 Steam turbine simulation and thermal stresses

To investigate thermal stresses during a start-up, a thermo-mechanic stress model of the rotor was made based on Can Gülen and Kim [39]. A one-dimensional model of heat exchange in radial direction was adopted, where the rotor underwent a stepchange in surface temperature. The stress was calculated on the rotor surface by applying the equations described in section 2.7.1. The thermal mass in the turbine was modelled as a unit length cylinder with the radius $r _ { 0 }$ , a simplification described by Grosso et al. [16]. The transient heat conduction was calculated by using Equation (2.17), where $r ^ { * }$ , Bi and $F o$ varied both over time and radial location in the rotor.

The steam properties at every time step were determined by a mathematical function which interpolated in steam tables, with pressure and temperature as the input. This was needed for determination of HT C described in Equation (2.11). The Biot number compared the convective heat transfer to the conductive (Eq. 2.16) and was later used to determine the coeficients $\zeta _ { n }$ and $C _ { n }$ , which solved the non-dimensional temperature diference $\theta ^ { * }$ at every radial location at any time.

When the temperature gradient in the rotor was determined, the stress described in Equation (2.19) was calculated. The only parameter in this expression that varied over time was the rotor temperature diference $\Delta T .$ , all other parameters were assumed to be constant. The lowest values of the data on material propertieis were chosen when running the transient simulation and calculations.

Based on the chosen material, a relationship between stress and number of cycles to failure, also known as an S-N curve, was obtained from the material database CES EduPack [44]. As CES EduPack provided the equation of the S-N curve, an accurate calculation of the relationship with the available data was given as input, for which an S-N curve could be constructed. The stress ratio included in the equation was set to 0, which implied undirectional testing starting with zero stress [45]. By considering the maximum stress levels, their corresponding number of cycles to failure, could be derived from the curve.

## 3.1.2 Equivalent operating hours

The equivalent operating hours were calculated by following the approach presented in the theory-section 2.7.1 based on Aminov et al. [18]. As the thesis only consid ered fatigue due to thermal stresses, variables involving creep were neglected. These were $b _ { i }$ in Equation (2.20) and $Z _ { C }$ in Equation (2.21).

With data assumptions on the expected lifespan of the rotor and expected years in service, as well as scenario input on the number of ran cycles, the total number on EOH was calculated by adding overall operating hours to Equation (2.20). Hence, the equation was written as:

$$
E O H = O H + \Big [ ( a _ { c o l d } \cdot n _ { c o l d } ) + ( a _ { w a r m } \cdot n _ { w a r m } ) + ( a _ { h o t } \cdot n _ { h o t } ) \Big ]
$$

Lastly, the total EOH could be divided by the expected years in service, $Y$ , to obtain the yearly EOH. The calculated values were used as input to the computation of maintenance costs.

## 3.1.3 Reliability due to fatigue

The maintenance cost calculations required values on reliability followed by MTTF and MTTR in order to allow computation. As the rotor was exposed to three startup types, a stress model had to be designed considering varying stresses over a period of time in order to give accurate results. Simple reliability calculations could have been made by using only the i-th number of cycles to failure points from the S-N curve, but would then have neglected the scenario input in the methodology, which was an important factor.

By using the constructed S-N curve, followed by the thermal stress calculations, a Weibull distribution fit was conducted on the data in the <sup>Matlab</sup>-environment. The analysis gave the Weibull parameters $\beta$ and $\eta$ using a maximum likelihood estimation. Thereafter, the parameters were used to calculate the individual reliability of each start type over time using Equation (2.2).

As each start-up type corresponded to a certain reliability or probability of failure, the three reliability functions were weighted according to the number of scenario start types $n _ { i }$ . The cumulative reliability was then expressed as a weighted mean value of each individual reliability curve according to Equation (3.1), where the equation considered operational patterns and the damage caused by the start-up types according to Palmgren’s-Miners’ rule (Eq. 2.21).

$$
R _ { t o t } ( t ) = \frac { n _ { c } R _ { c } ( t ) + n _ { w } R _ { w } ( t ) + n _ { h } R _ { h } ( t ) } { n _ { t o t } }\tag{3.1}
$$

The damage or lifetime usage of the rotor could further be determined by using a cumulative damage model. As the rotor is subject to damage due to both creep and thermal fatigue, a summation method taking both measurements into consideration is wise. Since the thesis only considered fatigue, creep was neglected. However, as

Banaszkiewicz [12] shows, the creep life expenditure could consume 55% or more of the rotor life, making creep an important factor to actually consider. Therefore, it was decided to not let the scenario input to the methodology exceed a fatigue damageability parameter of $Z _ { F } = 3 5 \%$ . This also allowed a 10% safety margin until the rotor would fail at $Z = 1$ . The damageability parameter was calculated by considering $Z _ { F }$ in Equation (2.21).

To obtain MTTF, the reliability was integrated over time as in Equation (2.3). Thereafter, the correlation between MTTF, MTTR and availability in Equation (2.4) were used to calculate MTTR. This required an assumption on the availability of the steam turbine, and was set to a typcial number of 94% [46]. This meant that 6% of the cases when the steam turbine was wanted to be used, it was not possible to use it due to a prohibiting event, for instance an unexpected failure. By rewriting Equation (2.4), the MTTR was computed the following way:

$$
\mathrm { M T T R } = \mathrm { M T T F } \cdot ( \frac { 1 } { A } - 1 )
$$

## 3.1.4 Maintenance cost calculations

The cost of maintenance was calculated and evaluated from an LCC-perspective for the maintenance policies FBM, TBM, CBM and OBM with respect to the three types of services INT, EXT and FWC. Equations (2.23)-(2.34) were used as the cost models to calculate the maintenance costs. Input data to the calculations were defined in section 3.2, along with computed numbers on reliability, MTTF, MTTR and EOH.

Further, as the maintenance cost calculations on the TBM-policy required a time interval on the intended inspection intervals, these were calculated by using Equation (3.2). It was determined to use the typical EOH-inspection interval in the industry today, known from section 2.7.2, namely every 25 000-th EOH, in order to recalculate $E _ { T B M }$ to normal operating hours.

$$
E _ { T B M } = { \frac { 2 5 ~ 0 0 0 ~ E O H } { E O H ~ f o r ~ e a c h ~ s c e n a r i o } } \cdot O H _ { Y } ~ [ h ]\tag{3.2}
$$

## 3.1.5 Result presentation

The last part of the methodology illustrates the element that would show and visualize the results in a way that they would assist and support discussions. At first, all calculated maintenance costs were normalized to SEK/MWh in order to create reasonable numbers to compare. The normalization was done by taking each total maintenance cost and divide it by the expected power output from a 150 MW steam turbine during a 25-year period with 8000 yearly operating hours.

Thereafter, the maintenance costs were plotted in a 3D-plot with the maintenance cost per produced MWh on the z-axis, the total number of start-ups in the specific scenario on the y-axis and the number of cold starts in the scenario on the x-axis. This way of presenting the costs was believed to give an interesting indication of how cold starts could impact on the maintenance cost, and how a shift of start type could change the costs. The graphs were further recommended to also be supported by tables containing numbers for easier interpretation.

## 3.2 Determination of data input

In order to compute and confirm the functioning of the developed methodology, data had to be defined. This section presents the data that were needed in order to perform the calculations. Each following subsection present the determined data input for each part of the methodology framework along with explanations on how the data was defined.

## 3.2.1 Material properties

The detailed properties on the material in steam turbines are often disclosed and intellectual properties of the OEM. It is however commonly known that the rotor material in a steam turbine is generally a steel alloy where the composition aims to minimizing failures due to creep, fatigue, cracking, corrosion and erosion [47]. The chosen alloy for the thesis was a CrMoV-alloy (chromium alloy) suggested by Osgerby [47] and also used in lifetime assessments by Banaszkiewicz [12]. This steel alloy is suitable for structural parts in severe service conditions and is also known as AISI 10 [44]. Table 3.1 presents the material properties on the alloy, that were used in the transient start-up simulations and construction of the AISI 10 S-N curve, where the values were obtained from the material database CES EduPack [44].

Table 3.1: Material properties for the chromium alloy AISI 10. Data was retrieved from the material database CES EduPack [44].
<table><tr><td>Property</td><td>Symbol</td><td>Value</td><td>Unit</td></tr><tr><td>Young&#x27;s modulus</td><td>E</td><td>208 - 218</td><td>GPa</td></tr><tr><td>Yield strength</td><td> $\sigma _ { Y S }$ </td><td>973 - 1740</td><td>MPa</td></tr><tr><td>Tensile strength</td><td> $\sigma _ { T S }$ </td><td>1210 - 1980</td><td>MPa</td></tr><tr><td>Elongation</td><td>€</td><td>6.6 - 15.5</td><td>% strain</td></tr><tr><td>Poisson&#x27;s ratio</td><td>ν</td><td>0.285 - 0.295</td><td>1</td></tr><tr><td>Fatigue strength at  $1 0 ^ { 7 }$  cycles</td><td></td><td>292 - 522</td><td>MPa</td></tr><tr><td>Fatigue stress range</td><td></td><td>235 - 648</td><td>MPa</td></tr><tr><td>Density</td><td>ρ</td><td>7740 - 7890</td><td> $\mathrm { k g / m ^ { 3 } }$ </td></tr><tr><td>Thermal conductivity</td><td>λ</td><td>36.8 - 39.8</td><td> $\mathrm { W / m } . { ^ { \circ } \mathrm { C } }$ </td></tr><tr><td>Specific heat capacity</td><td> $C _ { p }$ </td><td>292 - 522</td><td> $\mathrm { J / k g . ^ { \circ } C }$ </td></tr><tr><td>Thermal expansion coefficient</td><td> $\alpha _ { e x p }$ </td><td>11.3 - 11.8</td><td>µ strain/°C</td></tr></table>

## 3.2.2 Steam turbine data

Three types of start-ups were simulated on a steam turbine. This created a need for classifying what kind of start-up that was being run. The classification is often turbine-specific, but, usually, one categorizes the start-ups based on the metal temperature in the rotor or more simplified after the number of stand-still duration hours. For this thesis, Table 3.2 defined for which measured metal metal temperatures in the rotor that the respective start-up type belonged to. The start-up conditions were defined accordingly to Grosso et al. [16] and Banszkiewicz [48]. The range of operating temperatures were confirmed by experienced people in the industry based on conducted interviews [32] and concluded as suitable for a steam turbine with a possible power output of approximately 150 MW.

Table 3.2: Start-up ramping conditions for cold, warm and hot steam turbine start-ups.
<table><tr><td>i</td><td>Start type Metal temperature  $T _ { m }$ </td><td>Stand-still duration Start-up time</td><td> $t _ { i }$ </td></tr><tr><td>Cold</td><td> $< 1 5 0 ~ ^ { \circ } \mathrm { C }$ </td><td>&gt; 108 h</td><td>180 min</td></tr><tr><td>Warm</td><td> $1 5 0 \textrm { - } 4 1 0 \textrm { ^ { o } C }$ </td><td> $1 6 - 1 0 8 { \mathrm { ~ h ~ } }$ </td><td>105 min</td></tr><tr><td>Hot</td><td> $> 4 1 0 ~ ^ { \circ } \mathrm { C }$ </td><td> $< 1 6 \mathrm { ~ h ~ }$ </td><td>40 min</td></tr></table>

![](images/62ed2b1048a14b57e08fe482207ef17b10eb1cd01fd40d62e30a24692f79f44c.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/62ed2b1048a14b57e08fe482207ef17b10eb1cd01fd40d62e30a24692f79f44c.jpg

    ```plaintext
- **Equipment names**: Not specified in the image.
- **Equipment tags and identifiers**: Not specified in the image.
- **Electrical components**: None visible in the image.
- **Mechanical components**: Mass flow, pressure, temperature are mechanical parameters.
- **Connections between components**: No connections shown; these are individual parameter trends over time.
- **Flow direction**: Mass flow increases over time. Pressure and temperature remain constant or change gradually with time.
- **Numerical values**:
  - Mass flow: ~0 to >125 kg/s
  - Pressure: ~70 bar to 100 bar
  - Temperature: ~480°C to 560°C
- **Units**: 
  - Mass flow: [kg/s]
  - Pressure: [bar]
  - Temperature: [°C]
- **Warning limits**: Not specified in the image.
- **Operating limits**: Not specified in the image.
- **Labels and annotations**:
  - Cold start, Warm start, Hot start
  - Time [min] on x-axis for all graphs
  - Mass flow [kg/s], Pressure [bar], Temperature [°C] on y-axis respectively.

- **Maintenance information**: None visible in the image.
- **Operational information**: The graph shows different operational scenarios (cold, warm, hot start) with varying mass flow rates over time. Pressure and temperature remain relatively constant or change gradually during these starts.
```
      
Figure 3.2: Start-up curves for cold, warm and hot starts.

The values in Table 3.2 were given as input to the transient simulations and calculations of the steam turbine, along with the needed start-ups curves presented visually in Figure 3.2. The start-up curves described how each start-up was controlled by keeping respect to permissible temperatures in the turbine, hence thermal stresses. This was done by monitoring and controlling the inlet mass flow rate of steam, the pressure and the temperature over time. At a real plant, this is monitored and controlled by the use of a by-pass valve. Closer details on the specific turbine are being disclosed.

Other important steam turbine data were the material properties on the rotor from section 3.2.1, the dimensionless Biot numbers from Table 2.2 and an assumption on the rotor radius. A rotor radius was defined as $r _ { 0 } = 0 . 3 \ m$ , a typical value according to Can Gülen and Kim [39].

## 3.2.3 Equivalent operating hours data

The first step in the EOH calculations was to define the individual time coeficients $a _ { i }$ for each start-up type. These calculations used numbers on the rotor lifespan $\tau _ { l i f e }$ and the maximum number of cycles to failure of each start type, $N _ { i }$ . Data on the expected rotor lifespan was taken from Aminov et al. [18], while the numbers of cycles to failure were given from the calculations on thermal stresses.

As the scope of the thesis only considered fatigue, no data was needed for creep calculations. However, as the rotor should still consider the creep impact during its lifetime, the damagebility parameter $Z$ was set to 1 in Equation (2.21), for which failure typically occurs after the exposure to both creep and fatigue [18]. Further, for each start-up type $i ,$ a scenario input was required stating the expected number of total starts during the lifetime $n _ { i }$ , as well as expected years in service, Y . The number of start-ups are later defined in the scenario definitions, see section 3.3, and the required data inputs for the EOH-calculations were:

Variables: $\tau _ { l i f e } = 2 0 0 \ 0 0 0 \ [ \mathrm { h } ]$

$$
\begin{array} { r l } { Z } & { { } = 1 \left[ - \right] } \end{array}
$$

$$
\begin{array} { r l } { Y } & { { } = 2 5 \ [ \mathrm { Y e a r s } ] } \end{array}
$$

## 3.2.4 Maintenance cost data

The LCC-calculations on maintenance costs required numbers on calculated data for reliability, ${ \mathrm { M T T R } } ,$ MTTF, EOH as well as input data on consuming costs and time deviations. Table 3.3 is stating all the variables that were needed in the LCCcalculations and the determined values. Argumentation on how they were defined follow after the table.

Table 3.3: Data input used for calculations of LCC maintenance costs.
<table><tr><td>Variable</td><td>Value</td><td>Unit</td><td>Explanation</td></tr><tr><td> $L _ { I N T }$ </td><td>700</td><td> $\mathrm { S E K / h }$ </td><td>Internal labour cost</td></tr><tr><td> $L _ { E X T }$ </td><td>1400</td><td> $\mathrm { S E K / h }$ </td><td>External labour cost</td></tr><tr><td> $\mathit { L } _ { \mathit { F W C } }$ </td><td>10 000 000</td><td>SEK</td><td>External contract labour cost</td></tr><tr><td> $F _ { F B M }$ </td><td>137 000</td><td>SEK</td><td>Fixed and consumable FBM cost</td></tr><tr><td> $F _ { T B M }$ </td><td>205 500</td><td>SEK</td><td>Fixed and consumable TBM cost</td></tr><tr><td> $F _ { C B M }$ </td><td>274 000</td><td>SEK</td><td>Fixed and consumable CBM cost</td></tr><tr><td> $F _ { O B M }$ </td><td>205 500</td><td>SEK</td><td>Fixed and consumable OBM cost</td></tr><tr><td> $C _ { C D }$ </td><td>5 000 000</td><td>SEK</td><td>Cost of collateral damage</td></tr><tr><td> $C _ { L P }$ </td><td>30 000</td><td> $\mathrm { S E K / h }$ </td><td>Cost of lost production</td></tr><tr><td> $C _ { S P }$ </td><td>5 000 000</td><td>SEK</td><td>Cost of spare parts</td></tr><tr><td> $S D T$ </td><td>2160</td><td>h</td><td>Delay time of spare part acquisition</td></tr><tr><td> $M D T _ { i n t }$ </td><td>1</td><td>h</td><td>Mean delay time of internal response</td></tr><tr><td> $M D T _ { e x t }$ </td><td>168</td><td>h</td><td>Mean delay time of external response</td></tr><tr><td> $\sigma _ { S P }$ </td><td>80</td><td>%</td><td>Factor neglecting spare part change</td></tr><tr><td> $\sigma _ { F W C }$ </td><td>75</td><td>%</td><td>Warranty considerations</td></tr><tr><td> $T M$ </td><td>0.75·MTTR</td><td>h</td><td>Time for maintenance intervention</td></tr><tr><td>ξ</td><td>100</td><td>%</td><td>Interventions causing downtime</td></tr><tr><td> $p _ { 1 }$ </td><td>70</td><td>%</td><td>Fraction of replacement decisions</td></tr><tr><td> $p _ { 2 }$ </td><td>5</td><td>%</td><td>Fraction of unrecognized failures</td></tr></table>

Labour costs - $L _ { I N T } , L _ { E X T }$ and $\mathit { L } _ { \mathit { F W C } }$

Two experienced internal workers were assumed to be working full time at the scenario plant. They were assumed to be employed with a fixed monthly gross salary, but together costing the plant owner 700 SEK per hour. For the external service, an hourly fee of 1400 SEK/h was assumed to be billed to the plant for every MTTRhour when performing maintenance. And lastly, the external contract service was expected to cost 10 000 000 SEK a year, as the contract service reduces the cost of spare parts due to better warranty conditions $( \sigma _ { F W C } )$ and do not have any spare part delay times or afiliated fixed costs.

## Fixed and consumable costs - $F _ { F B M } , F _ { T B M } , F _ { C B M }$ and $F _ { O B M }$

Keatly et al. [17] have created a methodology that forecasted the lifetime start costs and considered long-term service agreement with minor and major overhaul costs as their cost input. Kumar et al. [19] have on the other hand mapped the capital and maintenance cost for diferent types of power plants which resulted in big cost spreads among the same type of power output. The assumptions on costs for fixed and consumable costs were hence a dificult one, as it is impacted by plant type, size, configuration, age etc. [19]. However, an assumption had to be made in order to make the computations possible. For the FBM-policy, fixed costs were expected to be lower than the other policies as the policy is basically holding the spending until something breaks down. When using the other maintenance policies, the costs were expected to be higher as tools and consumables are continuously used due to its preventive characteristics. Therefore, $F _ { F B M }$ was determined to be 1000 SEK/MW<sub>el</sub> for a 150 MW power plant. TBM and OBM occurring periodically were set to 1500 $\operatorname { S E K } / M W _ { e l }$ and for CBM it increased even more due to increasing consumables of things such as lubrication, oil, seals etc. and was set to 2000 $\mathrm { S E K } / M W _ { e l }$ for the same plant output. The costs were then multiplied with the expected yearly operating hours and expected yearly power output.

## Consequential costs $\mathrm { ~ - ~ } C _ { C D } , C _ { L P }$ and $C _ { S P }$

The cost of collateral damages, $C _ { C D } .$ , caused by failures was a dificult variable to estimate since there are many circumstances impacting on how a failure could impact dependable systems. Also, if a failure is detected early and an operator is shutting down the process, the collateral damage may be less severe than a heavy failure causing a ruined turbine. As these collateral damages could include everything from broken bearings to broken turbine blades, the cost range is wide and was therefore set to 5 000 000 SEK. The cost of lost production, $C _ { L P }$ was calculated based on the possible total power output multiplied with the market price for electricity. It was assumed that the producer was loosing 50% in revenue during unplanned disruptions while the other 50% were production costs. The current electricity price was set by Nord Pool and approximated to be 400 SEK/MWh [49]. For a steam turbine with a power output of 150 MW, $C _ { L P }$ was therefore calculated to 30 000 SEK/h. Another challenging variable to determine was the cost for spare parts, $C _ { S P }$ . When assumed that the steam turbine is running in such a way that the aim is to make it last the expected years in service, Y , the rotor must seldom be replaced. However, if replaced, the price could be several millions SEK depending on turbine size and customization. Hence, the cost of for $C _ { S P }$ was set to 5 000 000 SEK.

## Delay time variables - SDT , $M D T _ { i n t }$ and $M D T _ { e x t }$

As most steam turbines are more or less custom made [32], it was assumed that there is rather limited availability to spare parts on the market. Long transports could also have an impact on the delay time. The spare part delay time for an unforeseen error SDT was therefore set to 3 months, 2160 h. Important to denote is that this delay time can vary from case to case as companies can work diferently with spare part management and keep higher or lower levels of parts in stock [50]. The mean delay time internally, $M D T _ { i n t }$ , for the response of the internal maintenance crew was set to 1h, considering that the workers sometime can be busy with another broken component, but sometimes also faster and can respond immediately to the call. Considering $M D T _ { e x t }$ , it was assumed that the service company was having a remote location of the plant and also having more plants to maintain. That caused the mean delay time to be set to seven days.

## Deviation parameters - $\sigma _ { S P }$ and $\sigma _ { F W C }$

The deviation parameters are coeficients that are paying respect to the fact that not all maintenance interventions necessarily need a spare part change. In case of a service contract with the OEM, the coeficient $\sigma _ { F W C }$ also considers that spare parts may be covered by warranties [30]. In case of internal and external maintenance the coeficient $\sigma _ { S P }$ , was assumed to be 0.8, meaning 80% of all interventions needed a spare part change. When using external contract service with warranty consideration, another 5% of the spare part changes were assumed to be covered by warranties. σ<sub>FW</sub> <sub>C</sub> was then defined as 0.75.

Time variables - $T M , \xi , p _ { 1 }$ and $p _ { 2 }$

The T M-variable is the time needed to carry out a preventive maintenance task, and can according to Reina et al. be estimated as 0.7-0.8 of the MTTR [30]. The variable was hence determined as 75% of the MTTR. The ξ-variable is a coeficient that considers that maintenance interventions can take place either by causing or not causing downtime of the machine, in other words, a stop of the system [30]. It was assumed that all of the failures were causing unplanned stoppages of the steam turbine which needed interventions or tasks that could not be done without stopping the machine. When using a CBM-policy, it must be taken into consideration that the instruments cannot recognize all deviations and is hence creating monitoring uncertainties. This introduced the variables $p _ { 1 }$ and $p _ { 2 }$ , where $p _ { 1 }$ is a coeficient that considers the percentage of life the component in which it is possible to make decisions about a components replacement [30]. This coeficient was assumed to be high for a steam turbine, since they are often monitored by several instruments. The coeficient $p _ { 1 }$ was set to 70%. The coeficient $p _ { 2 }$ is the small fraction of failures that can occur without being recognized by the monitoring instruments [30]. As in line with the previous argument and with instrument highly sensitive, this number was assumed to be rather low and was set to 5%.

## 3.3 Scenarios and results analysis

In order to answer one of the objectives of the thesis, how the maintenance cost may change with operational patterns, it was of interest to define scenarios reflecting the expected future impact of increased shares of renewable energy sources [1]. The scenarios were determined to reflect a base line scenario on the number of start-ups and increases based on expected figures. All the defined scenario are presented in Table 3.4.

Banaszkiewicz et al. analyzed the number of start-up at a 200 MW thermal power plant during 43 387 real operating hours 267 start-ups occurred [11]. As they also performed detailed analyzes on the casing temperature of the turbine, they were also able to classify the start-ups into the start-up categories cold, warm and hot. The numbers were taken for usage in this thesis and recalculated to match the defined lifetime input $\tau _ { l i f e }$ . These number of starts were defined as scenario 1 (S1), presented in Table 3.4.

In 2017, Schill et al. [51] analyzed how the start-up costs and the number of startups of thermal power plants are expected to change with an increasing share of non-dispatchable power generation. They also gave figures on the expected increasing number of starts. It must be denoted that this analysis was made based on the German market, where the primary product from the thermal plants is electricity [32] and where the renewable generation is on the forefront since the country is aiming at a drastic increase of renewable energy sources until 2050 [51]. With the number of starts in 2013 as a reference, to an expected scenario in 2020, Schill et al. expected an increase of 4% in terms of number of starts. After another 10 years, until 2030, an 81% increase was expected relative the case in 2013.

In this thesis, scenario 2 (S2) was then determined to represent an increase of 40% as a case in between the 2013-case from Schill et al. [51] and their 81% expected increase. Thereafter, scenario 3 (S3), was defined as a scenario with an 81% increase relative S1. And as previously pointed out, it was of interest in the thesis to study the impact of cold starts and how a shift from a cold to hot start would impact on the maintenance cost. Hence, a fourth scenario (S4) was determined to match the exact number of total start as in S3, but with another fraction of cold, warm and hot starts.

Lastly, another two scenarios were defined, scenario 5 (S5) and scenario 6 (S6). S5 was defined as one cold start every second month during a year and a hot start every second day. These numbers are not based on any type of reference, but wanted to be tested in relation to S6 to see how the methodology would respond when doing half the cold starts from S5, but twice as many hot starts from S5.

Table 3.4: Scenario definitions in terms of number of start-ups.
<table><tr><td rowspan="2">Start type  $i$ </td><td colspan="6">Scenarios</td></tr><tr><td>S1</td><td>S2</td><td>S3</td><td>S4</td><td>S5</td><td>S6</td></tr><tr><td></td><td> $n _ { i }$ </td><td> $n _ { i }$ </td><td> $n _ { i }$ </td><td> $n _ { i }$ </td><td> $n _ { i }$ </td><td> $n _ { i }$ </td></tr><tr><td>Cold Warm</td><td>144</td><td>187</td><td>261</td><td>185 261</td><td>150 0</td><td>75 0</td></tr><tr><td>Hot</td><td>995 102</td><td>1294 133</td><td>1801 185</td><td>1801</td><td>4563</td><td>9125</td></tr><tr><td>Total</td><td>1241</td><td>1641</td><td>2247</td><td>2247</td><td>4713</td><td>9200</td></tr></table>

# Results

The results chapter focuses on presenting the computational results of the testing of the developed methodology and describe the impact and relations the chosen scenarios has to maintenance costs. The presentation follows the same structure as the bottom elements in the visual mapping of the methodology framework shown in Figure 3.1, sectioned as:

• Steam turbine simulation

• EOH and Reliability

• Maintenance cost calculations

• Result presentation

## 4.1 Thermal stresses on the steam turbine rotor

The constructed rotor model computed thermal stresses with respect to the dynamic start-up conditions of the steam turbine. The results from the transient simulations are presented in Table 4.1, as the maximum thermal stresses due to the temperature gradient and when they occurred in time t after the start initiation. The last column of the table is stating the maximum number of cycles to failure that was obtained from the constructed S-N curve, see Figure 4.3.

![](images/ef98525af54373351999faffbf98c4e88de43fc1736177879aab06c8827ec9df.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/ef98525af54373351999faffbf98c4e88de43fc1736177879aab06c8827ec9df.jpg

    ```json
{
  "Temperature_distributions": {
    "Axis_labels": {
      "x_axis": "Time [min]",
      "y_axis": "Temperature [°C]"
    },
    "Trends": {
      "Core": "Increasing trend",
      "r=0.1 m": "Increasing trend",
      "r=0.2 m": "Increasing trend",
      "Surface": "Increasing trend"
    },
    "Thresholds_and_abnormal_regions": {
      "Cold": 150°C,
      "Warm": 300°C,
      "Hot": 400°C
    }
  }
}
```
      
Figure 4.1: The step changes of the temperature distributions of cold, warm and hot start-ups. The distribution is shown for four points of the rotor.

Figure 4.1 presents the temperature distributions in four points of the rotor of a cold, warm and hot start-up. The maximum temperature diferences between the rotor core and the surface caused the maximum thermal stresses in the rotor. For the presented start-ups, the largest temperature diference between the core and the surface occurred when performing a cold start. At t = 18 min, after start initiating the resulting maximum stress was calculated to 421 MPa. How each of the start-up stresses were varying in the rotor is shown in Figure 4.2. These calculated temperature diferences and stress levels corresponded well to similar calculations performed by Grosso et al. [16] and Casella and Pretolani [52].

![](images/4054547e4d2315fb3cb83054c9c7ecf6a08f4e79fd0b0b6df8657eef69b5b3d3.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/4054547e4d2315fb3cb83054c9c7ecf6a08f4e79fd0b0b6df8657eef69b5b3d3.jpg

    ```json
{
  "Stress profiles": {
    "Equipment names": ["Cold", "Warm", "Hot"],
    "Units": {"Stress": "[MPa]", "Time": "[min]"},
    "Trends": [
      {"Cold": {"Initial Stress": "0 MPa", "Peak Stress": "420 MPa", "Final Stress": "150 MPa"}},
      {"Warm": {"Initial Stress": "300 MPa", "Peak Stress": "370 MPa", "Final Stress": "20 MPa"}},
      {"Hot": {"Initial Stress": "0 MPa", "Peak Stress": "400 MPa", "Final Stress": "15 MPa"}}
    ],
    "Abnormal regions": [
      {"Cold": {"Region": "[90-130 min]", "Observation": "Stress increases sharply"}},
      {"Warm": {"Region": "[60-80 min]", "Observation": "Stress decreases sharply"}}
    ]
  }
}
```
      
Figure 4.2: The calculated stress-profiles for each start-up type, showing how the stresses were varying in the rotor over time.

![](images/afd68cd40648676f57c370a84bfcdb72721dc74cf84f343385948db6647881bd.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/afd68cd40648676f57c370a84bfcdb72721dc74cf84f343385948db6647881bd.jpg

    The image provided is an S-N curve graph. Here are the extracted details:

1. **Equipment names**: None visible in this image.
2. **Equipment tags and identifiers**: None visible in this image.
3. **Electrical components**: None present in this image.
4. **Mechanical components**: The graph represents mechanical fatigue data, specifically stress (S) versus number of cycles to failure (N).
5. **Connections between components**: None as it is a single graph.
6. **Flow direction**: Not applicable for an S-N curve.
7. **Numerical values**:
   - Stress: 200 MPa to 650 MPa
   - Number of cycles to failure: \(10^3\) to \(10^7\)
8. **Units**:
   - Stress [MPa]
   - Number of cycles to failure [-] (dimensionless)
9. **Warning limits**: Not explicitly marked, but the graph shows typical fatigue life data.
10. **Operating limits**: The curve indicates the maximum stress for a given number of cycles before failure.
11. **Labels and annotations**:
    - \(N_C = 885\): Number of cycles at 420 MPa
    - \(N_W = 9786\): Number of cycles at 350 MPa
    - \(N_H = 101265\): Number of cycles at 300 MPa
12. **Maintenance information**: None provided in the image.
13. **Operational information**: The graph shows how stress affects the number of cycles to failure, which is crucial for material fatigue analysis.

This S-N curve is used to determine the maximum allowable stress that a material can withstand without failing within a specified number of cycles under cyclic loading conditions.
      
Figure 4.3: S-N curve for the used alloy material AISI 10 in the steam turbine rotor, where stress levels are marked in order to find maximum number of cycles $N _ { i }$

The constructed S-N curve of the alloy material was used to plot the calculated stresses, $\sigma _ { m a x }$ , and hence obtain the maximum cycles to failure for each start type, $N _ { i }$ . The obtained cycles are shown in Figure 4.3 as well as in Table 4.1. It can further be concluded that 1 cold start, corresponds approximately to 10 warm or 100 hot starts. This is in line with what Venkatesh et al. [14] stated based on experience, strengthening that the rotor model is likely to perform accurately.

When changing the scenario in the rotor model, no changes were done on the temperature distributions, stresses or maximum cycles to failure. This was due to the unchanged process parameter number that were not included in the scenarios. However, if letting the ramping times, temperatures or pressures in the steam turbine vary, the resulting changes in the rotor model would create diferent results. This opens up to discussions of a more advanced methodology.

Table 4.1: Results of the transient start-up simulations with the maximum temperature diferences, the maximum stresses and when they occurred in time after start initiation.
<table><tr><td>Start type i</td><td>Maximum temp. diff.  $\Delta T _ { m a x _ { i } }$ </td><td>Maximum stress  $\sigma _ { m a x _ { i } }$ </td><td>Time t</td><td>Cycles to failure  $N _ { i }$ </td></tr><tr><td>Cold</td><td>125 ℃</td><td>421 MPa</td><td>120 min</td><td>885</td></tr><tr><td>Warm</td><td>108 ℃</td><td>366 MPa</td><td>75 min</td><td>9786</td></tr><tr><td>Hot</td><td> $8 0 ~ ^ { \circ } \mathrm { C }$ </td><td>318 MPa</td><td>28 min</td><td>101 265</td></tr></table>

## 4.2 Equivalent operating hours calculations

The first step in the EOH-calculations was to determine the time coeficient $a _ { i }$ for each start-up type. With the defined input data and the calculated results on $N _ { i }$ 2 the following time coeficients were obtained:

$$
a _ { c o l d } = \frac { 2 0 0 ~ 0 0 0 } { 1 } \cdot \frac { 1 } { 8 8 5 } = 2 2 6 ~ h
$$

$$
a _ { w a r m } = { \frac { 2 0 0 ~ 0 0 0 } { 1 } } \cdot { \frac { 1 } { 9 7 8 6 } } = 2 0 ~ h
$$

$$
a _ { h o t } = { \frac { 2 0 0 ~ 0 0 0 } { 1 } } \cdot { \frac { 1 } { 1 0 1 ~ 2 6 5 } } = 2 ~ h
$$

These calculated numbers on EOH can be compared to the actual start times presented in Table 3.2. From a comparison, it can be concluded that the EOH-times are significantly larger. The EOH-values were also confirmed in interviews to be of reasonable size [32] compared to real data, but it must be denoted that the calculations are highly depended on specific steam turbines. The calculations of EOH for each scenario resulted in a maximum number of hours of continuous operation, which are presented in Table 4.2.

Table 4.2: The operating hours for continuous operation for each scenario.
<table><tr><td rowspan="2">Variable</td><td colspan="6">Scenarios</td></tr><tr><td>S1</td><td>S2</td><td>S3</td><td>S4</td><td>S5</td><td>S6</td></tr><tr><td>OH [h]</td><td>147 352</td><td>131 592</td><td>104 624</td><td>149 368</td><td>156 974</td><td>164 800</td></tr><tr><td>OHY [h]</td><td>5 894</td><td>5 264</td><td>4185</td><td>5 975</td><td>6 279</td><td>6 592</td></tr></table>

The individual time coeficients remain the same throughout the methodology, and hence the total EOH-values as well, unless no changes would have been made in the transient simulations. In a real turbine, where the ramping conditions are easily varied, the outcome would likely be diferent and could result in varying EOH-values for each unique start.

## 4.3 Reliability analysis

The results of the performed analysis of the Weibull distribution gave the parameters presented in Table 4.3. It can be seen in the table that the scale parameters varys, depending on the maximum number of cycles to failure $N _ { i }$ , but are close to similar for the shape parameter $\beta .$ This can be explained by the same type of failure distribution, only having varying stress levels.

Table 4.3: Calculated Weibull distribution parameters of a cold, warm and hot start up, based on their number of cycles to failure.
<table><tr><td>Start type  $i$ </td><td>Shape parameter  $\beta$ </td><td>Scale parameter  $\eta$ </td></tr><tr><td>Cold</td><td>1.6262</td><td>489.2</td></tr><tr><td>Warm</td><td>1.6190</td><td>5399.8</td></tr><tr><td>Hot</td><td>1.6182</td><td>55866.1</td></tr></table>

![](images/34ae7721f235957f860e72e8ec29f3a543df698dc2961890e40894a5d9271f39.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/34ae7721f235957f860e72e8ec29f3a543df698dc2961890e40894a5d9271f39.jpg

    ```json
{
  "image_type": "graph",
  "axis_labels": {
    "x_axis": "Cycles [-]",
    "y_axis": "Reliability [%]"
  },
  "trends": {
    "Cold": "High reliability initially, then decreases sharply.",
    "Warm": "Moderate reliability initially, then decreases more gradually than Cold.",
    "Hot": "Lowest initial reliability, but increases and stabilizes at a higher level compared to Cold."
  },
  "thresholds": {
    "Reliability": [0]
  },
  "abnormal_regions": {
    "Cold": "[10^2, 10^3]",
    "Warm": "[10^4, 10^5]",
    "Hot": "[10^5]"
  }
}
```
      
Figure 4.4: Reliability curves for each start-up type.

With the reliability of each start-up type plotted individually shown in Figure 4.4, it can be seen that the reliability is decreasing earlier for a cold start than for a warm or hot start-up, for the same number on N . This is in line with the hypothesis of shorter lifetime expenditure the rotor is sufering, due to the higher stress levels of a cold start. As the rotor is impacted by diferent reliability characteristics, an overall reliability was calculated by considering the scenario input as a weighted contribution. Considering the MTTF originating from the reliability, it was expressed in terms of cycles, referring to start cycles until the rotor fails without a specification on failure cause. Therefore, MTTF do not consider neither impact from stops or continuous operation. The results on reliability for each scenario are presented in Table 4.4.

Table 4.4: Numbers on reliability, MTTF and life usage of each scenario after the total number of cycles.
<table><tr><td>Scenario</td><td>Cycles  $n _ { t o t }$ </td><td>C</td><td>No. of start-type W</td><td>H</td><td>Reliability  $R ( t = n _ { t o t } )$ </td><td>MTTF Cycles</td><td>Life usage  $Z _ { F }$ </td></tr><tr><td>1</td><td>1241</td><td>144</td><td>995</td><td>102</td><td>81.42 %</td><td>8 041</td><td>26.54 %</td></tr><tr><td>2</td><td>1641</td><td>187</td><td>1294</td><td>133</td><td>77.82 %</td><td>8 051</td><td>34.48 %</td></tr><tr><td>3</td><td>2247</td><td>261</td><td>1801</td><td>185</td><td>71.12 %</td><td>8 047</td><td>48.08 %</td></tr><tr><td>4</td><td>2247</td><td>185</td><td>261</td><td>1801</td><td>88.83 %</td><td>40 703</td><td>25.35 %</td></tr><tr><td>5</td><td>4713</td><td>150</td><td>0</td><td>4563</td><td>95.06 %</td><td>48 459</td><td>21.46 %</td></tr><tr><td>6</td><td>9200</td><td>75</td><td>0</td><td>9125</td><td>93.97 %</td><td>49 633</td><td>17.49 %</td></tr></table>

When analyzing the results in Table 4.4, starting with S1 to S4, one can see a decreasing trend in reliability from S1 to S2 to S3. In terms of MTTF, the explanation on the varying results is caused by rounded values. Since MTTF is a measure defined as the integral of $R ( t )$ from 0 to ∞, the diference lies in the shape of the curve creating the integrated area. Rounding up or down the values from the scenario input could hence impact on the diference in MTTF. The range from 8041 cycles for S1 to 8051 cycles for S2, is therefore not considered as faulty. Looking at fatigue life usage $Z _ { F }$ , the usage in S3 is exceeding the set threshold of $Z _ { F } = 3 5 \%$ . The chance of failure in combination with the discarded creep, is now significant and one must suggestively investigate this scenario closer in more aspects than just fatigue. In S4, when swapping numbers of starts from S3, the life usage drops to a lower value than S1, due to its lesser number of warm starts and only slightly increased number of cold starts. The reliability is higher than in any of S1, S2 or S3 and the measure on MTTF has five folded to 40 703 cycles. This clearly shows how the diferent types of starts is impacting on the rotor lifetime.

In case of S5 and S6, the reliability is dropping from 95.05% for S5 to 93.97% for S6. Even though the number of cold starts is cut to half, one must keep in mind that the total number of starts in the scenario has almost been doubled. If considering S6 and stepping back in its scenario history, one would obtain a higher value of reliability when N would be 4713. That explains the higher number on MTTF. In terms of fatigue life usage $Z _ { F } ,$ the lower value in S6 is simply due to the shift towards more hot starts, impacting less on the rotor rupture than cold starts.

## 4.4 LCC-calculations on maintenance costs

For the equations using a time-based maintenance (TBM) policy, the inspection interval, $E _ { T B M }$ , was calculated for each scenario and resulted in intervals ranging from 16 883 to 21 279 hours. In the equations on an opportunity-based maintenance (OBM) policy, there was instead a t-variable present. With the variable defined as the interval of an opportunity window, it was defined as $t = 8 0 0 0$ for the cases with relatively low MTFF (8000 cycles) and $t = 1 6 0 0 0$ for cases with higher MTTF. This reflects a risen opportunity once per year or once every second year.

The results on the LCC-computations are presented in Table 4.5. The table presents each scenario by expressing the maintenance cost in SEK/MWh. As the methodology evaluates four maintenance policies and three labour services, there are 72 possible combinations of the costs. It must further be pointed out, that if the calculated scenario exceeded the threshold of $Z _ { F } = 3 5 \%$ , the cost of spare parts was ten-folded as the threshold limit was considered as a failure. This meant that such a scenario would increase the cost of spare parts significantly. Table 4.5 is followed by visualization of the given numbers in 3D-plotted graphs in Figure 4.5, 4.6 and 4.7.

Table 4.5: LCC results for maintenance expressed in SEK/MWh for internal (INT), external (EXT) and contract maintenance (FWC), applied to the four policies: failure- (FBM), time- (TBM), condition- (CBM) and opportunity-based maintenance (OBM).
<table><tr><td>Labour</td><td>Policy</td><td>S1</td><td>Maintenance costs S2</td><td>S3</td><td>[SEK/MWh] S4</td><td>S5</td><td>S6</td></tr><tr><td>INT</td><td>FBM</td><td>42.71</td><td>42.68</td><td>58.21</td><td>25.92</td><td>27.03</td><td>27.62</td></tr><tr><td></td><td>TBM</td><td>13.12</td><td>13.66</td><td>28.78</td><td>25.31</td><td>22.72</td><td>21.29</td></tr><tr><td></td><td>CBM</td><td>14.32</td><td>14.32</td><td>34.96</td><td>12.77</td><td>12.88</td><td>12.93</td></tr><tr><td></td><td>OBM</td><td>25.55</td><td>25.56</td><td>55.56</td><td>30.40</td><td>27.90</td><td>26.78</td></tr><tr><td>EXT</td><td>FBM</td><td>41.04</td><td>41.01</td><td>56.55</td><td>22.88</td><td>24.08</td><td>24.71</td></tr><tr><td></td><td>TBM</td><td>8.78</td><td>9.34</td><td>24.50</td><td>21.54</td><td>18.84</td><td>17.34</td></tr><tr><td></td><td>CBM</td><td>12.44</td><td>12.43</td><td>33.08</td><td>10.89</td><td>11.00</td><td>11.05</td></tr><tr><td></td><td>OBM</td><td>21.69</td><td>21.71</td><td>51.70</td><td>26.85</td><td>24.24</td><td>23.07</td></tr><tr><td>FWC</td><td>FBM</td><td>25.78</td><td>25.77</td><td>40.33</td><td>21.98</td><td>22.24</td><td>22.37</td></tr><tr><td></td><td>TBM</td><td>16.63</td><td>17.16</td><td>31.38</td><td>28.82</td><td>26.24</td><td>24.82</td></tr><tr><td></td><td>CBM</td><td>16.02</td><td>16.02</td><td>36.66</td><td>14.56</td><td>14.65</td><td>14.71</td></tr><tr><td></td><td>OBM</td><td>28.83</td><td>28.85</td><td>56.97</td><td>33.88</td><td>31.38</td><td>30.26</td></tr></table>

When analyzing the values in Table 4.5, starting with S1 to S4, it is of interest to remember the analysis and conclusions derived from Table 4.4. It must also be remembered that S1 is the base line scenario and that S3 is exceeding the Z = 35% threshold. Comparing S1 to S2 for all labour and policy types, there is no significant trend noted as the proportion of starts remain the same after the 40% increase and both scenarios make sure not to trespass life usage. For S3, the spare part cost is ten-folded for all labour and policy cases and it can be seen that the cost per MWh has radically increased. In terms of S4, there are interesting changes taking place and when comparing S4 against S3 as well as S1, the diference in the chosen numbers of start-up types becomes present. With a higher number of hot starts in S4 than the other cases and rather low numbers on cold and warm stars, an FBMpolicy becomes the cheapest in an S4-case if it would be of interest to be using. When comparing the TBM-policy among first four scenarios, it is seen to be more expensive for S4, which could be explained by the higher reliability from Table 4.4 and interventions will become unnecessary and lead to extra costs even for a long time after the rotor investment.

Considering the two scenarios S5 and S6, both of the scenarios are making the Zlimit and there is actually not a big diference among the cost for the policies relative to each other for the two scenarios. From Table 4.5 in combination with Table 4.4, one can determine that a scenario with more cold starts, S5, would cost almost the same as a scenario with half as many cold starts but twice as many hot starts, S6. It is therefore possible to double the number of starts and almost keeping the same maintenance cost by just adjusting the proportion of the number of start types. This is in line with severity notation by Venkatesh et al. stating that 1 cold start

## equals 100 hot starts [14].

To conclude from Table 4.5, an FBM-policy would generally be the most expensive, with a contribution by high collateral damage costs. It can, however, be seen that when having a higher portion of hot starts and less cold, the FBM-policy decreases in expensiveness and becomes more interesting. One must though remember the possible consequences that could occur if letting the machinery just run until it fails leading to unforeseen production shutdowns, eventual collateral damages, long spare part deliveries etc. It must also be pointed out that the presented costs are only overhead maintenance costs and do not vary with the changed number of starts. According to Schill et al. an increased number of starts by 81% is expected to lead to increased start costs of 119% [51]. An interesting case would be to investigate that correlation to maintenance. Further, as theory presented, preventive maintenance is known to be cheaper than reactive [7] and would actually be able to increase the numbers on the reliability after an intervention has been performed. In the current methodology, this is discarded as the reliability is untouched after an intervention, leading to shorter lifetimes than it actually should. This could most certainly be impacting on the maintenance costs.

![](images/0351471f03ebc16f3468b560f0f235201564810992137004e587146c8d68f0ee.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/0351471f03ebc16f3468b560f0f235201564810992137004e587146c8d68f0ee.jpg

    The image provided appears to be a 3D graph related to internal maintenance costs. Here's the extracted information:

1. **Equipment names**:
   - FBM (Failure-Based Maintenance)
   - TBM (Time-Based Maintenance)
   - CBM (Condition-Based Maintenance)
   - OBM (Other-Based Maintenance)

2. **Equipment tags and identifiers**:
   - S1, S2, S3, S4, S5, S6

3. **Maintenance cost units**: SEK/MWh
4. **Total starts**: The x-axis represents the total number of starts.
5. **Cold starts**: The y-axis represents cold starts.

The graph shows maintenance costs for different equipment and maintenance strategies across various start conditions (total starts and cold starts). Each point on the graph corresponds to a specific combination of total starts, cold starts, and maintenance cost in SEK/MWh.
      
Figure 4.5: A visual comparison of the internal maintenance costs for FBM-, TBM-, CBM- and OBM-policies. The maintenance cost is expressed in SEK/MWh on the z-axis, the total number of starts in the scenario on the y-axis and lastly the number of cold starts in the scenario on the x-axis. The scenarios are indicated by the vertical lines and pointed out using the prefix S.

Figure 4.5 supports the numbers presented in Table 4.5 and shows how the internal maintenance cost can be represented as a function of operational patterns in terms of both the total number of starts and the amount of cold starts, that are impacting on the costs. The graph shows the presence of expensive costs for FBM- and OBMpolicies for all scenarios and the competing two policies CBM and TBM.

![](images/7e8c294dd2550e4b0f6205abad46210419c9f8af508464155ce85ca10f1b37fd.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/7e8c294dd2550e4b0f6205abad46210419c9f8af508464155ce85ca10f1b37fd.jpg

    The image provided appears to be a 3D scatter plot graph related to external maintenance costs. Here's the extracted information:

1. **Equipment names**:
   - FBM (Failure-Based Maintenance)
   - TBM (Time-Based Maintenance)
   - CBM (Condition-Based Maintenance)
   - OBM (Other-Based Maintenance)

2. **Equipment tags and identifiers**:
   - S1, S2, S3, S4, S5, S6

3. **Maintenance cost units**: SEK/MWh
4. **Total starts**: The x-axis represents the total number of starts.
5. **Cold starts**: The y-axis represents cold starts.

The graph shows maintenance costs for different equipment types (FBM, TBM, CBM, OBM) across various start conditions and cold starts. Each point on the plot corresponds to a specific combination of these factors and their associated maintenance cost in SEK/MWh.
      
Figure 4.6: A visual comparison of the external maintenance costs for FBM-, TBM-, CBM- and OBM-policies.

![](images/76db7b77f79a82efd8d028ced464d72ce1bd04775f96c69b6c6909b69bd52687.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\Maintenance and operational patterns\images/76db7b77f79a82efd8d028ced464d72ce1bd04775f96c69b6c6909b69bd52687.jpg

    The image provided appears to be a 3D scatter plot graph titled "Maintenance with framework contract." The axes are labeled as follows:

- X-axis: Cold starts [-]
- Y-axis: Total starts [-]
- Z-axis: Maintenance cost [SEK/MWh]

The legend indicates the following equipment types:
- FBM (represented by circles)
- TBM (represented by stars)
- CBM (represented by diamonds)
- OBM (represented by squares)

There are data points labeled with identifiers S1, S2, S3, S4, S5, and S6. The maintenance cost values range from approximately 0 to 60 SEK/MWh.

No electrical components or mechanical connections are visible in the image; it is a maintenance cost analysis graph for different types of equipment under framework contracts.
      
Figure 4.7: A visual comparison of maintenance costs using a framework contract for FBM-, TBM-, CBM- and OBM-policies.

Looking at Figure 4.6, it can be seen that the costs for external maintenance policies are close to the internal, making it hard to distinguish any new trends based on the graphics. When having the supporting numbers on hand from Table 4.5, the small diference between internal and external maintenance service can be explained by analyzing the equations in section 2.8. It can then be concluded that the only difference between internal and external maintenance is the labour costs and the time at the site.

For maintenance service based on a framework contract, the costs are changing compared to the other cases, as the equations are defined slightly diferent. This might be, since Figure 4.7 shows that the OBM-policy is the most expensive policy due to the fact that maintenance is carried out no matter if it is necessary or not. With a contract, this creates forced high costs. A CBM-policy is among the cheapest policies to use as the contracted company is responsible for monitoring and replacing parts whenever it is needed. This also impacts on the previously expensive FBMpolicy with the other services, since the cost of a failed machinery is taken on by the contracted company, becomes the contracted company’s cost.

On the bottom line, any conclusions will not be drawn in terms of suggested maintenance based on the obtained results. The developed methodology and tool aims to support the discussions on maintenance where many possible discussion points have been highlighted. Even though it could be possible to conclude which scenario, policy and labour service should be recommended to be used, there are many external parameters impacting on the decision. These parameters refer to, but are not limited to the primary power plant product (heat or electricity), the demand, requirements and restrictions from the market and its energy system and pre-requisites for the plant owner. A discussions of the developed tool and the method will continue in the discussions chapter.

# Discussion

The developed methodology shows how an operating parameter like the number of starts may be used to estimate the lifetime expenditure of the rotor, and how it relates to the maintenance costs. The method could, thus, be used for guidance in design of new operational modes for thermal power plants for more volatile future energy market scenarios. Further more, the view on maintenance of production systems has been seen as a development over time, previously being a necessary evil, but now a strategic question [7], the discussions on how and when maintenance should be performed is a key driver in a plant strategy [8]. Not only will maintenance help to increase the reliability of the plant resources, such as the steam turbine rotor, but could also help to gain economic advantages by decreasing the chances of unwanted downtime.

A relevant notation in the discussion of this thesis is whether or not an expected change in the number of starts is relevant for all markets. The increased share of renewable energy sources will probably only afect the operational pattern at thermal power plants in markets where electricity is the primary product. As for an instance, most plants in Sweden are focusing on the delivery of heat as primary product [32], this is what drives the plants revenue and not the demand on electricity. The generated electricity at these plants is more of a bi-product and the plants are therefore not interested to schedule their operations accordingly in the same extent, especially in a short term perspective. This thesis work would therefore be more suitable for markets like Denmark, Germany and the Netherlands where electricity is what drives the revenue at many thermal power plants and where the operational pattern of the plants will be significantly afected by the increasing share of renewables.

## 5.1 Methodology and sensitivity

The results shows how a scenario with a diferent numbers of start-ups connects to rupture of the rotor in the steam turbine. With an increasing need of start and stops and possible load ramps due to varying net loads, there will be changes in the maintenance costs for power plant owners. Section 4.4 elaborated on how the costs in an LCC-perspective would change based on the scenarios, but as there are many input parameters to consider, one must also be aware of the possibly varying results from case to case. Therefore, note that the aim of the thesis has never been to suggest how future maintenance should be performed at power plants, but to act as a supporting tool in discussions on how to evaluate diferent perspectives.

All the defined input data originates in some form from assumptions as described in the methodology chapter. Some assumptions are more reasonable than others since some are highly challenging to estimate without insight. A comparable example of this is how internal salaries for internal maintenance labour is easier to assume rather than costs for collateral damages or spare parts in case of rotor failures on a steam turbine in the considered size. The costs can range from a couple of thousands SEK to millions depending on the severity. Furthermore the turbine might be custom made by the OEM and spare part can take a year to design, produce and deliver in a worst case scenario [32]. For the results, this could mean miss-calculated costs indicating the wrong correlation between operational pattern and maintenance.

In addition, material properties of the rotor could vary over its axis due to diferent geometrical dimensions, certainly impacting on the results. In the rotor model, the rotor was defined as a cylinder of infinite length for simplifications, but would preferably be modelled in a FEM-software with its real manufactured dimensions. That would increase the accuracy of the results even more as it would consider a more advanced mathematical relationship. This could also help to evaluate both tensile and compressing stresses in geometric complex locations. By changing some of the material properties, one could expect other results in temperature diferences in the rotor model, impacting the stresses and eventually the results on maintenancen costs.

When considering how the methodology is computing the input data, only fatigue due to start-ups was considered. In a more extensive model with more detailed scenarios, there would be reasonable to add support for the impact of creep impacted by the temperature diference as well as support for the impact of load changes on the turbine due to the more volatile operational patterns. This could be done today by changing the start-up times, where the temperature diferences would be even bigger resulting in even more severe thermal stresses. This would then lead to an even shorter lifetime with sustained numbers on start-ups. This is a case likely case in the future when a sudden drop could appear in the non-dispatchable power generation.

The fact that preventive interventions are performed on the steam turbine rotor was also discarded in the methodology. In a real case, a precautionary action would likely contribute to an extended lifetime and hence an increase in reliability by elevating the reliability curve at the current time. Also, as Schill et al. [51] present in their work on how renewable energy sources are expected to impact on increased start-up costs, questions on increased maintenance costs would also be of interest. Today, the methodology is not considering an increase in the assumed overhead costs. This is becoming clear when assessing S1 with S2 and one can see that the cost per is almost the same. Hence, questions are raised that varying costs could be applied to the maintenance cost data.

In a management perspective, it is also of interest to ask oneself what is wanted. In the methodology today the cost of maintenance is calculated in a life cycle costing perspective where the goal is to consider all the costs afiliated with maintenance during the rotor lifetime. How the results are then used is a management question. Do one want to minimize the costs and use the cheapest policy? Or does one want to minimize the number of interventions by just monitor the health on a computer screen? Or is it of interest to discard the costs and just focus on maximum availability by taking every possible chance to increase or maintain the reliability of the rotor? It could even be the case that reliability is the key, if the plant is working close to industrial production, for example the oil industry, and losing one day of production would mean the cost of several rotors. These are questions that the methodology is not considering as of today and could be possible work for the future, preparing for how to plan, schedule and optimize the maintenance. Another maintenance concept, rather than LCC would also be of interest to use, for the evaluation of maintenance and is often sometimes based on a company level. Perhaps the change towards an even more dynamic electricity market would have more use of a life cycle profit approach, where one is estimating how the equipment can instead contribute to profit [27]. The importance of the maintenance strategy would hence depend on the role of the power plant in the energy system.

However, the methodology successfully manages to provide results based on the available input data and is indicating the general knowledge in the industry, that preventive maintenance is often cheaper than reactive maintenance [7]. It is however hard to tell what changing operational patterns would mean in terms of possible changes in maintenance. Today, most plant owners are working actively with preventive maintenance on a daily, weekly, monthly and yearly basis, often with directions and schedules from the OEMs [32], [33]. It is often common that the plant owners are using frameworks with contract maintenance where expertise is brought in on revision periods for performing and leading maintenance on set intervals. This shows strong applications of TBM-policy usage in the industry, and at the same time having CBM-policies for which hundreds of sensors are monitoring the turbines in parameters such as temperatures, pressures and most importantly vibrations [32].

The way electricity is consumed as a product is also constraining how maintenance of the power producing equipment can be performed. Any other type of typically produced product, is most likely able to be put on delay and let the customer wait for delivery if the producing equipment breaks down or has to be maintained. But as electricity cannot be stored at a reasonable cost today, the production must constantly meet the demand and the customer or consumer cannot be put on hold in the same way. This is creating a need of regarding maintenance of power plants connected on the same grid in a holistic perspective, as all plants cannot shut down their power production at the same time. There must be detailed planning and scheduling behind the decisions, needing a time variable behind the planning. Certainly, the machinery can also be condition monitored, but if all power plants are running FBM-policies and break down at the same time, there would not only be consequences for each plant but for substantial parts of our society since it is relying heavily on the power grid. This strongly highlights the need for usage of the developed tool with clearly defined market conditions along with its production from

diferent energy sources.

## 5.2 Experience for future work

The rotor model could eventually have been developed by the help of a dynamic simulation model in a software like Dymola. In this project, it was investigated to do it without including the entire steam cycle, but it was discovered that for a proper Dymola simulation, the turbine model required good implementation of boundary conditions, or having a close-cycle model with control structures and bypass valves, which was too challenging without close plant collaboration or knowledge of the exact process configuration. The work on a dynamic model would however be recommended to be done in future work by following previous research approaches [53]–[55], in order to define more complex scenarios containing more parameters and get a more extensive picture of the start-up results.

For this thesis, if was concluded that the usage of a more simple start-up rotor model would be enough to create a transient simulation based on work by Can Gülen and Kim [39]. The developed rotor model considered temperatures, pressures and times, which could possibly be changed due to diferent scenarios by the user with the goal to match other types of load ramps and start-ups than those defined for the specifically considered turbine. This was however not included in the defined scenarios for the thesis. Further, the current transient model did not vary the Nu-, Re- or Pr-numbers which would be the case in a more mathematical complex model. This type of model could then have been for instance made in Dymola and in the combination of an FEM tool. But the simplifications that were made in the thesis, are still of such character that they are describing the rotor start-ups and the relationships taking place, and are certainly good enough for the scope of this thesis.

There was also an initial thought on calculating reliability using a more complicated stress model with an inverse power law relationship using an underlying Weibull distribution. This was tried out by the usage of ReliaSoft ALTA Pro, but was eventually discarded as there was not time to find a solution creating a seamless integration from the transient simulations and later over to the cost model. Hence, it was decided to develop the complete methodology in <sup>Matlab</sup> even though specialized software could have given more accurate results for the diferent models. An even more dynamic rotor model could have also considered dynamic life limits of the turbine by giving condition monitored parameters as input to reliability calculations.

Another challenge in the project was the acquisition of data. Most of the data was collected from other research projects where collaborations had been conducted with power plant owners. From the interviews, it was learned that before the 2000s, an international organization used to gather data on maintenance performance from power plant members all across the world and later printed publications for all organization members. This type of data was not found in the literature review performed in this project, but could have helped to gain more interesting insights.

The interviews also concluded that more and more maintenance is being handed over to the OEMs [32], which most likely don’t want to disclose data to the public nor competitors, as it can be important information for their research and development. No conclusions have been drawn based on this, but would be in line with the evolving view of shifting maintenance issues into a strategic question [7]. Another interesting insight from the interviews, was the view on external maintenance in the industry. The current trend is that maintenance is carried out either internally or by the OEM, especially when it comes to critical parts as the steam turbine [32], [33]. So even if the LCC-results in the thesis pointed towards external maintenance, this might not be preferred in the reality.

When Bokrantz et al. studied how maintenance is expected to change in the manufacturing industry until 2030, using Delphi-based scenarios, it was found with high probability that the evolution of digitalized manufacturing will introduce a high presence of data collection and the usage of data analytics and big data management [56]. It was expected that maintenance organizations will use the data to identify patterns, root causes and make decisions, eventually using support decision systems. An example of this is the developed digital twin by DecisionLab on a Siemens Gas Turbine, named the Agent-based Turbine Operations & Maintenance model. The digital model monitors maintenance repair and overhaul of Siemens’ aero-derivative gas turbine division using live data available in their supply chain [57] and helps to do better data-driven decision makings and to predict KPIs as well as overwatch maintenance operations.

With this amount of data gathering and pattern identification, it would also be possible to connect events and scenarios to variable maintenance costs and see how the costs follows the scenarios and turbine usage more dynamically and accurately rather than using overhead costs. Though this requires a close collaboration with industry.

# 6

# Conclusion

This master’s thesis has developed a method to relate the thermal stresses caused by frequent starts and stops to maintenance costs of a steam turbine rotor by considering temperature diferences in the rotor and relating them to lifetime and costs. The development of the method is based on previous work experience from industry.

This thesis shows that the cost of maintenance can be estimated depending on the operational pattern and maintenance policies, constrained by scenario prerequisites. The developed methodology is considered possible to be used for initial testings in real cases but must be reviewed and given real input data for accurate validation. The application can be made for plants on those markets where electricity is driving the revenue and not heat. In an even further extent, the purpose of the methodology is also believed to eventually be achieved by enabling cost eficiency in the power industry.

Furthermore, from the application of the proposed method to a set of scenarios three main conclusions may be drawn:

1. A higher number of starts impact the steam turbine rotor maintenance. The extent of the impact depends on what type of starts that are initiated on the turbine. A cold start causes more wear on the rotor and will contribute to a faster rupture of the rotor, which results in higher maintenance costs - 1 cold start equals almost 100 hot starts. The number of cold starts is, therefore, important to consider if one wants to aim for a minimized maintenance cost.

2. It is generally known that preventive maintenance is preferred to reactive maintenance, where collateral damages could be serious and extremely costly when considering a steam turbine. Also, in case of a framework contract service, the opportunity-based maintenance policy is most expensive. This could be explained by the original equipment manufacturer often wants to perform more maintenance than the plant owner is expecting.

3. The method is supporting the industry standard of today. It is common that the original equipment manufacturer is involved in the maintenance service, providing a vast experience on how to run, care and repair the machines. This is typically done on time-based intervals and decision from condition-based parameters. As the turbine machinery is a rather complex and expensive system with demands on high availability and reliability, the cost for lost production in high peak seasons is devastating for plant owners.

# Future work

The first step in future work is suggested to be the questioning of what is really wanted to be obtained from the methodology, asking questions like; What should the application of the methodology be able to indicate? How does one want to use the results from the application of the methodology? Is there something in the methodology today that is not in line with future desires? Secondly, the authors are emphasizing the need for accessing data for proper input. If possible, it is also recommended to validate the results from the rotor and cost model in terms of the degree of accuracy and relate those results to the previously discussed areas of improvements. Then, prioritization can be done on what must first be adjusted before continuing the development of the methodology.

With the expected volatile and dynamic operational patterns, the authors are also suggesting the development of the methodology to become more dynamic and to allow more changes of parameters over time. It should then be possible to compute the results cumulatively and to use more extensive boundary conditions for the whole process. Assuming a severe scenario is given as input, resulting in a break down earlier than the expected rotor lifetime. At the moment, the developed methodology will not consider those cases, other than increasing the spare part costs. In reality, this would likely impact more critically and it must therefore be scenarios in the methodology on how to handle such cases. An example would be if a new rotor is purchased after a breakdown and the reliability must then be reset.

As the developed methodology also focuses on the start-ups of a steam turbine, a more extensive and dynamic simulation model could help to investigate other critical components of the production process that are of interest. This could help to identify the approach on maintenance strategies not only for the steam turbine rotor but also the whole plant.

The methodology is also suggested to be implemented with simple planning and scheduling algorithms, that can predict suitable maintenance windows based on conditions such as forecasted demand, prices and production from renewable energy sources, as well as planned stops in other power plant, fuel prices and full company economic insights. This could be done by using economic dispatch models where wind speed, solar radiation and power demand could be used as random input variables. When and if involving this type of a more extensive dynamic and economic support, the cost of maintenance would be possible to relate to the produced product in a more precise way and calculated regarding how it varies with changed conditions. This would also create a good support for the identification of KPI:s and how they can be optimized. It would furthermore make it possible to let the methodology act as an even more advanced tool, supporting discussions in other perspectives, where it might even be possible to find new ways of working with the maintenance of thermal power plants.

## References

[1] J. Gil, A. Caballero, and A. J. Conejo, “Power Cycling: CCGTs: The Critical Link Between the Electricity and Natural Gas Markets”, IEEE Power and Energy Magazine, vol. 12, no. 6, pp. 40–48, Nov. 2014, <sup>issn</sup>: 1540-7977. <sup>doi</sup>: 10.1109/MPE.2014.2347631.

[2] B. Kriström and R. Brännlund, “Välfärdsefekter av olika kraftproduktionssystem - En förstudie inom EFORIS”, Tech. Rep., 2016. [Online]. Available: https: //energiforskmedia.blob.core.windows.net/media/19702/valfardsefekter-avolika-kraftproduktionssystem-energiforskrapport-2016-277.pdf.

[3] A. Stoppato, A. Mirandola, G. Meneghetti, and E. Lo Casto, “On the operation strategy of steam power plants working at variable load: Technical and economic issues”, Energy, vol. 37, no. 1, pp. 228–236, Jan. 2012, <sup>issn</sup>: 03605442. <sup>doi</sup>: 10.1016/j.energy.2011.11.042.

[4] P. Jonsson and S.-A. Mattsson, Manufacturing Planning and Control. London: McGraw-Hill Education, cop. 2009, 2009, pp. 88–90, <sup>isbn</sup>: 978-0-07-711739-9.

[5] K. Van den Bergh and E. Delarue, “Cycling of conventional power plants: Technical limits and actual costs”, Energy Conversion and Management, vol. 97, pp. 70–77, Jun. 2015, <sup>issn</sup>: 01968904. <sup>doi</sup>: 10.1016/j.enconman.2015.03.026.

[6] A. Benato, S. Bracco, A. Stoppato, and A. Mirandola, “Dynamic simulation of combined cycle power plant cycling in the electricity market”, Energy Conversion and Management, 2016, <sup>issn</sup>: 01968904. <sup>doi</sup>: 10.1016/j.enconman. 2015.07.050.

[7] L. Pintelon and A. Parodi-Herz, Complex System Maintenance Handbook, ser. Springer Series in Reliability Engineering. London: Springer London, 2008, ch. 2, pp. 22–48, <sup>isbn</sup>: 978-1-84800-010-0. <sup>doi</sup>: 10.1007/978-1-84800-011-7.

[8] M. Bellgran and K. Säfsten, Production Development. London: Springer London, 2010, <sup>isbn</sup>: 978-1-84882-494-2. <sup>doi</sup>: 10.1007/978-1-84882-495-9.

[9] M. Gopalakrishnan, A. Skoogh, A. Salonen, and M. Asp, “Machine criticality assessment for productivity improvement”, International Journal of Productivity and Performance Management, Jan. 2019, <sup>issn</sup>: 1741-0401. <sup>doi</sup>: 10.1108/ IJPPM-03-2018-0091.

[10] C. Vishnu and V. Regikumar, “Reliability Based Maintenance Strategy Selection in Process Plants: A Case Study”, Procedia Technology, vol. 25, no. RAER-EST 2016, pp. 1080–1087, 2016, <sup>issn</sup>: 22120173. <sup>doi</sup>: 10.1016/j.protcy.2016. 08.211.

[11] M. Banaszkiewicz, W. Radulski, and K. Dominiczak, “Advanced lifetime assessment of steam turbine components based on long-term operating data”, Archive of Mechanical Engineering, vol. 65, no. 4, pp. 579–597, 2018. <sup>doi</sup>: 10.24425/ame.2018.125443.

[12] M. Banaszkiewicz, “Multilevel approach to lifetime assessment of steam turbines”, International Journal of Fatigue, vol. 73, pp. 39–47, Apr. 2015, <sup>issn</sup>: 01421123. <sup>doi</sup>: 10.1016/j.ijfatigue.2014.10.009.

[13] L. Moroz, G. Doerksen, F. Romero, R. Kochurov, and B. Frolov, “Integrated Approach for Steam Turbine Thermostructural Analysis and Lifetime Prediction at Transient Operations”, Journal of Engineering for Gas Turbines and Power, vol. 140, no. 2, Oct. 2017, <sup>issn</sup>: 0742-4795. <sup>doi</sup>: 10.1115/1.4037755.

[14] K. Venkatesh, P. V. Raju, T. J. Kumar, and M. Tech, “Residual Life Assessment of 60 MW Steam Turbine Rotor”, International Journal of Scientific and Research Publications, vol. 2, no. 8, pp. 1–11, 2012. [Online]. Available: http://www.ijsrp.org/research-paper-0812/ijsrp-p0889.pdf.

[15] A. Musyafa, R. D. Noriyati, S. R. Dacosta, and S. Komayadi, “Reliability and Maintainability Assessment of the Steam Turbine Instrumentation System for optimization Operational Availability System at Fertilizer Plant”, Australian Journal of Basic and Applied Sciences, vol. 8, no. 13, pp. 132–139, 2014.

[16] M. Grosso, F. Sansoni, A. Sorce, M. Monti, F. Pascucci, and R. Razzoli, “Influence of Start-up Management on the Residual Life of a Large Steam Turbine Shaft”, International Symposium on Transport Phenomena and Dynamics of Rotating Machinery, pp. 1–9, 2016. [Online]. Available: http://isromacisimet.univ-lille1.fr/upload\_dir/finalpaper/145.finalpaper.pdf.

[17] P. Keatley, A. Shibli, and N. J. Hewitt, “Estimating power plant start costs in cyclic operation”, Applied Energy, 2013, <sup>issn</sup>: 03062619. <sup>doi</sup>: 10.1016/j. apenergy.2013.05.033.

[18] R. Z. Aminov, A. F. Shkret, and M. V. Garievskii, “Estimation of lifespan and economy parameters of steam-turbine power units in thermal power plants using varying regimes”, Thermal Engineering, vol. 63, no. 8, pp. 551–557, 2016, <sup>issn</sup>: 0040-6015. <sup>doi</sup>: 10.1134/s0040601516080012.

[19] N. Kumar, P. Besuner, S. Lefton, D. Agan, and D. Hilleman, “Power Plant Cycling Costs”, National Renewable Energy Laboratory (NREL), Golden, CO (United States), Tech. Rep. 3, Jul. 2012, pp. 245–248. <sup>doi</sup>: 10.2172/1046269.

[20] BCG - Boston Conculting Group, Embracing Industry 4.0 and Rediscovering Growth, 2019. [Online]. Available: https://www.bcg.com/capabilities/ operations/embracing-industry-4.0-rediscovering-growth.aspx.

[21] R. M. Montañés, M. Korpås, L. O. Nord, and S. Jaehnert, “Identifying Operational Requirements for Flexible CCS Power Plant in Future Energy Systems”, Energy Procedia, vol. 86, no. 1876, pp. 22–31, Jan. 2016, <sup>issn</sup>: 18766102. <sup>doi</sup>: 10.1016/j.egypro.2016.01.003.

[22] Svenska Kraftnät, National grid - The control room, 2019. [Online]. Available: https://www.svk.se/en/national-grid/the-control-room/.

[23] ——, Electricity Market, 2016. [Online]. Available: https://www.svk.se/en/ stakeholder-portal/Electricity-market/.

[24] ——, Electricity trade, 2016. [Online]. Available: https://www. svk. se/en/ national-grid/operations-and-market/electricity-trade/.

[25] P. Denholm, M. O’Connell, G. Brinkman, and J. Jorgenson, “Overgeneration from Solar Energy in California. A Field Guide to the Duck Chart”, no. November, 2015. <sup>doi</sup>: 10.2172/1226167.

[26] U.S Energy Information Administration, Increased solar and wind electricity generation in California are changing net load shapes, 2014. [Online]. Avail able: https://www.eia.gov/todayinenergy/detail.php?id=19111.

[27] C. Lundgren, A. Skoogh, and J. Bokrantz, “Quantifying the Efects of Maintenance - A Literature Review of Maintenance Models”, Procedia CIRP, vol. 72, pp. 1305–1310, 2018, <sup>issn</sup>: 22128271. <sup>doi</sup>: 10.1016/j.procir.2018.03.175.

[28] O. Isaksson, T. C. Larsson, and A. Ö. Rönnbäck, “Development of productservice systems: Challenges and opportunities for the manufacturing firm”, Journal of Engineering Design, vol. 20, no. 4, pp. 329–348, 2009, <sup>issn</sup>: 14661837. <sup>doi</sup>: 10.1080/09544820903152663.

[29] A. Rymaszewska, P. Helo, and A. Gunasekaran, “IoT powered servitization of manufacturing – an exploratory case study”, International Journal of Production Economics, vol. 192, pp. 92–105, Oct. 2017, <sup>issn</sup>: 09255273. <sup>doi</sup>: 10.1016/j.ijpe.2017.02.016.

[30] A. Reina, Á. Kocsis, A. Merlo, I. Németh, and F. Aggogeri, “Maintenance Decision Support for Manufacturing Systems Based on the Minimization of the Life Cycle Cost”, in Procedia CIRP, 2016, <sup>isbn</sup>: 3902273062. <sup>doi</sup>: 10 . 1016/j.procir.2016.11.117.

[31] M. Genrup and M. Thern, “Ny gasturbinteknik 2012-2014: Gas Turbine Developments”, Tech. Rep., 2013. [Online]. Available: https://energiforskmedia. blob. core.windows. net/media/19907/ ny - gasturbinteknik - 2012 - 2014 - gas - turbine-developments-elforskrapport-2014-20.pdf.

[32] L. Strömberg, Interview with Lars Strömberg, Gothenburg, May 2019.

[33] M. Rokka, Interview with Martin Rokka, Gothenburg, May 2019.

[34] International Electrotechnical Commission, Electropedia - Section 192-01: Basic Concepts, 2015. [Online]. Available: http://www.electropedia.org/iev/iev. nsf/index?openform&part=192.

[35] General Electric Power, Combioned-cycle power plant - How it works, 2019. [Online]. Available: https://www.ge.com/power/resources/knowledge-base/ combined-cycle-power-plant-how-it-works.

[36] F. Alobaid, N. Mertens, R. Starklof, T. Lanz, C. Heinze, and B. Epple, “Progress in dynamic simulation of thermal power plants”, Progress in Energy and Combustion Science, vol. 59, pp. 79–162, Mar. 2017, <sup>issn</sup>: 03601285. <sup>doi</sup>: 10.1016/j.pecs.2016.11.001.

[37] S. Sporre, “Validating and Modeling of Steam Turbine Temperature Distribution for Diferent Operational Cases”, Division of Thermal Power Engineering, Department of Energy Sciences, Lunds Tekniska Högskola (LTH), Lund, Sweden, Tech. Rep., 2018. [Online]. Available: http : / / lup . lub . lu . se / luur / download?func=downloadFile&recordOId=8963233&fileOId=8963234.

[38] M. Özisik, Heat Conduction. Raleigh, North Carolina: John Wiley & Sons, INC., 1998, vol. 2, <sup>isbn</sup>: 0-471-53256-8.

[39] S. Can Gülen and K. Kim, “Gas Turbine Combined Cycle Dynamic Simulation: A Physics Based Simple Approach”, Journal of Engineering for Gas Turbines and Power, vol. 136, no. 1, 2013, <sup>issn</sup>: 0742-4795. <sup>doi</sup>: 10.1115/1. 4025318.

[40] D. N. Dewangan, M. Kumar Jha, and Y. P. Banjare, “Reliability Investigation of Steam Turbine Used In Thermal Power Plant”, International Journal of Innovative Research in Science, Engineering and Technology, vol. 3, no. 7, pp. 14 915–14 923, 2014. [Online]. Available: http:// www. rroij. com/open - access / reliability - investigation - of - steam - turbineused - in - thermal - power - plant.pdf.

[41] J. Müller, “EOH - Equivalent operating hours of steam turbines”, PhD thesis, University of West Bohemia, 2017. [Online]. Available: https://dspace5.zcu. cz/bitstream/11025/28361/1/diploma\_thesis\_J\_Muller\_final.pdf.

[42] J. Latcovich, T. Åstrom, P. Frankhuizen, S. Fukushima, H. Hamberg, and S. Keller, “Maintenance and Overhaul of Steam Turbines”, in International Association of Engineering Insurers, Moscow, 2005. [Online]. Available: https: / / www . imia . com / wp - content / uploads / imiamembers / activities / past \_ conferences/maintenance\_of\_steam\_turbines.pdf.

[43] R. Kehlhofer, B. Rukes, F. Hannemann, and F. Stirnimann, “11. Development Trends”, in Combined-Cycle Gas and Steam Turbine Power Plants, 3rd Editio, Tusla, Okla: PennWell, 2009, ch. 11, pp. 277–286. <sup>doi</sup>: 10.5860/choice.29-2125.

[44] Granta Design, CES EduPack 2018 Software - Material Level 3, Cambridge, 2018. [Online]. Available: https://grantadesign.com/education/ces-edupack/.

[45] M. Gedeon, “Fatigue and stress ratios”, Technical Tidbits, no. 53, pp. 345– 350, 2013. [Online]. Available: https://materion.com/ - /media/files/alloy/ newsletters/technical-tidbits/issue-no-53---fatigue-and-stress-ratios.pdf.

[46] R. Kehlhofer, B. Rukes, F. Hannemann, and F. Stirnimann, “3.1.5 Comparison of Availability and Reliability”, in Combined-Cycle Gas and Steam Turbine Power Plants, 3rd Ed., Tusla, Okla: PennWell, 2009, ch. 3, pp. 11–34. [Online]. Available: https://app.knovel.com/hotlink/khtml/id:kt0088YRV1/combinedcycle-gas-steam/comparison-availability.

[47] S. Osgerby, “Steam turbines: operating conditions, components and material requirements”, in Structural Alloys for Power Plants, 2014. <sup>doi</sup>: 10 . 1533 / 9780857097552.1.22.

[48] M. Banaszkiewicz, “Steam turbines start-ups”, Transactions of the institute of fluid-flow machinery, no. 126, pp. 169–198, 2014. [Online]. Available: https: //www.imp.gda.pl/files/transactions/126/126\_12\_.pdf.

[49] Nord Pool Group, Price Development, 2019. [Online]. Available: https://www. nordpoolgroup.com/.

[50] D. Galar, P. Sandborn, and U. Kumar, Maintenance Costs and Life Cycle Cost Analysis. Boca Raton, FL: CRC Press, 2017, <sup>isbn</sup>: 978-1-4987-6954-9. <sup>doi</sup>: 10.1201/9781315154183.

[51] W. P. Schill, M. Pahle, and C. Gambardella, “Start-up costs of thermal power plants in markets with increasing shares of variable renewable generation”, Nature Energy, vol. 2, no. 6, pp. 1–6, 2017. <sup>doi</sup>: 10.1038/nenergy.2017.50.

[52] F. Casella and F. Pretolani, “Fast Start-up of a Combined-Cycle Power Plant : A Simulation Study with Modelica”, 6th Modelica Conference, pp. 3–10, 2006. [Online]. Available: https://www.modelica.org/events/modelica2006/ Proceedings/sessions/Session1a1.pdf.

[53] S. Gardarsdóttir, R. M. Montañés, F. Normann, L. O. Nord, and F. Johnsson, “Efects of CO2-Absorption Control Strategies on the Dynamic Performance of a Supercritical Pulverized-Coal-Fired Power Plant”, Industrial and Engineering Chemistry Research, vol. 56, no. 15, pp. 4415–4430, 2017. <sup>doi</sup>: 10.1021/acs.iecr.6b04928.

[54] R. M. Montañés, S. Gardarsdóttir, F. Normann, F. Johnsson, and L. O. Nord, “Demonstrating load-change transient performance of a commercial-scale natural gas combined cycle power plant with post-combustion CO2 capture”, International Journal of Greenhouse Gas Control, vol. 63, pp. 158–174, 2017. <sup>doi</sup>: 10.1016/j.ijggc.2017.05.011.

[55] L. O. Nord and R. M. Montañés, “Compact steam bottoming cycles: Model validation with plant data and evaluation of control strategies for fast load changes”, Applied Thermal Engineering, vol. 142, pp. 334–345, Sep. 2018. <sup>doi</sup>: 10.1016/j.applthermaleng.2018.07.012.

[56] J. Bokrantz, A. Skoogh, C. Berlin, and J. Stahre, “Maintenance in digitalised manufacturing: Delphi-based scenarios for 2030”, International Journal of Production Economics, vol. 191, pp. 154–169, Apr. 2017, <sup>issn</sup>: 09255273. <sup>doi</sup>: 10.1016/j.ijpe.2017.06.010.

[57] AnyLogic, ATOM: Digital Twin of Siemens Gas Turbine Fleet Operations, 2017. [Online]. Available: https://www.anylogic.com/atom-digital- twin-ofsiemens-gas-turbine-fleet-operations/.

## A

Appendix - Interview questions

Interview questions

Master’s Thesis work Date

Interviewers: Johan Egeland William Flodin

## Data management

The data gathered from the interview will be used as a background to the master’s thesis work at Chalmers University of Technology. The interview will be stored as a personal file and will only be published if the respondent gives his/her consent.

No personal data will be stored if the respondent does not give his/her consent. Personal data will not be shared.

## Ethics

This information is to ensure the respondent about his/her rights during the interview.

The respondent has no obligation to complete the interview and have the possibility to leave at any time. He or she have the possibility to retrieve all answers from the interview, if he or she wish so. There are no mandatory questions during the interview, which means that respondent choses which questions he or she answers. If the interview exceeds the stated time, the interviewer will ask the respondent to continue the interview. If the answer is no, the interview will end.

## General information

The aim of the project is to develop a first assessment method on how the maintenance cost would be varying based on changed start and stop of a steam turbine. This will be done by combining theory and methodologies from the fields of energy technology and production engineering, that will help to simulate, estimate and understanding the relation between maintenance and operational patterns in combined heat and power plants with a narrow focus on the steam turbine exposed to thermal stresses. The relation is assessed in terms of life cycle cost (LCC) for different maintenance policies and services related to different energy market scenarios.

The purpose of the development of the method is sought to be a beginning of a supporting tool that can help initial discussion of different maintenance strategies at power plants.

The interview is expected to take approximately 30 minutes.

## Interview questions.

The following questions are to be answered by the respondent over phone and answers are noted by the interviewer on a separate paper.

## 1. Background questions

a. Name

b. Current work tasks

c. For how long have you been working at the plant/in the industry?

## 2. General plant questions (if applicable, otherwise give from experience)

a. Please provide a short description of your plant process.

i. Size (MWth and MWel)

ii. Fuel type

iii. Main product

iv. Process configuration (GT, ST, HRSG etc.)

b. How is the plant operationally running over a year?

i. Load types?

ii. Revenue optimized for heat production or electricity?

c. What is the yearly average operating hours of your plant?

d. How many starts and stops of the plant do you perform on a yearly basis?

e. How many starts and stops do you perform in the categorization of cold, warm and hot starts on a yearly basis?

i. How are they defined?

## 3. General maintenance questions (if applicable, otherwise give from experience)

a. How are you working with maintenance of the plant today in general?

b. How are you scheduling and planning preventive maintenance tasks?

i. How are you working with maintenance during operational periods? Especially during the winter.

## 4. Maintenance of the steam turbine questions (if applicable, otherwise give from experience)

a. Which are the major crucial components in the steam turbine to monitor?

b. How are starts and stops of the steam turbine correlated to lifetime expenditure of the steam turbine and the previously mentioned components?

c. How are you working with maintenance of the steam turbine?

d. How are you scheduling and planning maintenance activities?

e. Does a change in the number of start and stops impact the planning of maintenance?

f. Is the concept of Equivalent Operating Hours (EOH) familiar when considering maintenance of the steam turbine? If yes, how are you using it?

g. With societal expectations on more volatile electricity prices in the future causing more cyclic operations, how do you expect this to impact the mechanical parts in the steam turbine?

i. Have you already noticed changes due to changing operational patterns?