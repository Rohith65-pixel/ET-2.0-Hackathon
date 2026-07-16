## Chapter 10

# Manufacturing of Thermal Power Generation Equipment

Gloria O. Pasadilla<sup>1</sup>

## 10.1. Industry Overview

The electric power industry has several major activities: power generation, transmission, and distribution. After electricity is generated, it passes through high voltage transmission lines. Power then goes to a substation where a transformer adjusts the voltage to a lower level to be distributed for consumer and industrial use. Figure 10.1 describes the electricity industry value chain, where power generation is shown to be an upstream activity. The focus of this case study is on power generation because the firm is a global player in power generation technologies.

Figure 10.1. Electricity industry value chain  
![](images/de3091431cc4a41a976b0097ebb7e35cda9ce4cc48aa9a4947646222724c5770.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\manufacturing-of-thermal-power-generation-equipment\images/de3091431cc4a41a976b0097ebb7e35cda9ce4cc48aa9a4947646222724c5770.jpg

    ```json
{
  "Equipment Names": [
    "Generating Station",
    "Generating Step Up Transformer",
    "Transmission lines (765, 500, 345, 230, and 138 kV)",
    "Substation Step Down Transformer",
    "Industrial Customer",
    "Residential Customer"
  ],
  "Equipment Tags and Identifiers": [
    "Black: Generation",
    "Blue: Transmission",
    "Green: Distribution"
  ],
  "Electrical Components": [
    "Generating Station",
    "Generating Step Up Transformer",
    "Transmission lines (765, 500, 345, 230, and 138 kV)",
    "Substation Step Down Transformer",
    "Industrial Customer",
    "Residential Customer"
  ],
  "Mechanical Components": [],
  "Connections between components": [
    "Generating Station to Generating Step Up Transformer",
    "Generating Step Up Transformer to Transmission lines (765, 500, 345, 230, and 138 kV)",
    "Transmission lines (765, 500, 345, 230, and 138 kV) to Substation Step Down Transformer",
    "Substation Step Down Transformer to Industrial Customer",
    "Substation Step Down Transformer to Residential Customer"
  ],
  "Flow direction": [
    "From Generating Station to Generating Step Up Transformer",
    "From Generating Step Up Transformer to Transmission lines (765, 500, 345, 230, and 138 kV)",
    "From Transmission lines (765, 500, 345, 230, and 138 kV) to Substation Step Down Transformer",
    "From Substation Step Down Transformer to Industrial Customer",
    "From Substation Step Down Transformer to Residential Customer"
  ],
  "Numerical values": [
    "765, 500, 345, 230, and 138 kV"
  ],
  "Units": [
    "kV"
  ],
  "Labels and annotations": [
    "Color Key: Black: Generation",
    "Blue: Transmission",
    "Green: Distribution"
  ]
}
```
      
Source: Courtesy of North American Electric Reliability Corporation (NERC)

The electricity industry has undergone deregulation all over the world, particularly through the privatization of many previously state-owned electricity companies and dismantled monopolies. In general, industry restructuring has carved out the power generation and retail supply segments (billing, metering, and installation) and introduced more market competition in these sub-industries to increase efficiency. In most places, transmission and distribution remain as monopolies, however, because it is unviable to build competing grids.

Power generation, the upstream part of the electricity value chain, involves the transformation of mechanical energy into electrical energy. Central to virtually all power generation is the turbine. When the blades on the shaft of a turbine is rotated the generator produces electricity through a process called magnetic induction<sup>2</sup>. The sources of energy that help to turn the blades of the turbine to generate electricity vary. Coal is the cheapest energy source but emits the most amount of harmful substances into the environment. Other energy sources are nuclear, natural gas, geothermal, hydro, as well as renewable sources like solar energy or wind.

Electricity generation causes more greenhouse gas emission than transportation<sup>3</sup>. Increased global awareness of the need for environmental sustainability has driven technological research to find alternative energy sources such as renewable energy, as well as to create improved designs of turbine and other power plant equipment that minimize emissions and reduce waste. The company in this study presents itself as a provider of both thermal power and environmental technologies because its new designs of power plant equipment use technologies that are environmentally friendly.

## 10.2. Background Information on the Firm<sup>4</sup>

The company is headquartered in Japan and is a big player in the production of thermal power generation machines and equipment. It has five production sites in Japan, but some products and/or parts and components are also manufactured in different continents either through a fully-owned subsidiary or a joint venture company. For example, in Asia, it has manufacturing plants in China, India, and the Philippines; In Europe, there is a manufacturing plant in Germany, while UK and Belgium have repair facilities; North America, Canada and the US have manufacturing plants. This is in line with the company strategy of manufacturing at sites close to where products are to be delivered. In total, its company brochure lists 54 different enterprises across the globe, either subsidiaries or joint venture companies that are engaged in either manufacturing, maintenance services and repairs, corporate functions and sales, or a combination of several functions. Of these 54 enterprises, it is significant to note that the majority are services companies.

The company’s major products are gas turbine combined cycle power plants; integrated gasification combined cycle power plants; boiler & turbine generation plants; geothermal power plants; gas turbines; boilers; steam turbines (Figure 10.2); generators; equipment peripheral to power generating plants; and fuel cells. Its research and development activities have helped to upgrade and redesign products either to minimize waste or limit harmful gas emissions and thus make electricity generation more environmentally friendly.

Beyond producing products for power plants, the company’s business also includes design, build, and maintenance of power plants; as well as a whole suite of after-sales services and support. Example of after-sales services include: 1) preventive maintenance which includes remaining life estimation service, maintenance schedule management, as well as maintenance personnel education programs; 2) original spare parts supply; 3) operation support to reduce power consumption or greenhouse gas emissions; 4) performance enhancement through operation control adjustments or equipment rehabilitation; and 5) integrity inspections, for example, for the high pressure and temperature vessel or piping in boilers.

Figure 10.2. Example of firm’s product: Steam engine and generator installed in an energy center in the United States  
![](images/bc1233bf3e7c5ecb9431ee579c60c9c5507ae28decaffcd4c6aada2146aec280.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\manufacturing-of-thermal-power-generation-equipment\images/bc1233bf3e7c5ecb9431ee579c60c9c5507ae28decaffcd4c6aada2146aec280.jpg

    ```json
[
  {
    "equipment_name": "Thermal Power Plant",
    "equipment_tags_identifiers": ["百色石火电站"],
    "electrical_components": [],
    "mechanical_components": [
      "Turbine",
      "Generator",
      "Boiler",
      "Cooling Tower"
    ],
    "connections_between_components": {
      "Turbine": "Generator",
      "Boiler": "Turbine",
      "Cooling Tower": "Thermal Power Plant"
    },
    "flow_direction": [
      {"source": "Boiler", "destination": "Turbine"},
      {"source": "Turbine", "destination": "Generator"},
      {"source": "Generator", "destination": "Electrical Grid"}
    ],
    "numerical_values": [],
    "units": [],
    "warning_limits": [],
    "operating_limits": [],
    "labels_and_annotations": ["百色石火电站"],
    "maintenance_information": [],
    "operational_information": []
  }
]
```
      
Source: Company website

## 10.3. Description of the Value Chain

This case study considers an EPCM (engineering, procurement, construction and maintenance) project where the firm may be the lead, or a member, of a consortium bidding for the construction of a power plant. There are, in fact, few EPC projects in which the company is the prime contractor; in most projects, the firm is only a member of a consortium where its primary responsibility is to supply the key machines and equipment for the power plant. The value chain, in this case, begins with the bidding stage, then moves to the equipment design and pre-construction of power plant stage, followed by the manufacturing and construction stage, and ends with the commissioning and operation of the power plant.

Other types of projects which do not involve construction from scratch also exist. Some projects may simply involve retrofitting and upgrading existing power plant facilities, or the construction of additional power plant features for environmental sustainability purposes. These types of projects will have a shorter value chain and will, in some respects, exhibit similar characteristics as an EPC turnkey project. On the other hand, the value chain described above omits an increasingly important part of the value chain, i.e. the disposal of old machines.

## Bidding stage

If the firm is the prime contractor or the leader of the consortium bidding for a project, it will identify potential partners, especially the local construction company that will carry out the plant construction. Then it will carry out research on the economic and legal environment, and the relevant policy framework, especially in respect of environmental policies. It will check the site or location of the power plant to assess if its geographical configuration necessitates major redesign or adjustments in the company’s existing equipment should it win the contract. It will carry out feasibility studies and a financial projection before submitting the bid.

In cases where the firm is only part of a consortium led by another prime contractor, the latter is considered the firm’s ‘customer’. Usually, these ‘customers’ are either utility companies or independent power providers in the economy where the power plant is to be built. In this case, all the feasibility studies and financial projection of the entire project are the responsibility of the prime contractor, but the firm also does its own research on the economic conditions, the legal environment of the economy, as well as assess the site or location of the proposed plant to be able to configure the right machines according to land type or topography. The firm participates in the preparation of the bid submission. In power plant projects, the cost that the case study firm provides to the consortium will typically constitute a major part of the total project cost and could help the consortium win or lose the bid.

## Design, pre-manufacturing and pre-construction of the power plant

If the firm is in-charge of the plant construction, it will typically outsource the construction work to a local subcontractor which is typically a construction or engineering company. The construction company then takes care of securing all the requisite government permits and often the overall project management of the construction process under the overall supervision of the firm.

Once the contract is awarded, the firm proceeds with the equipment design. Sometimes the design has either been done during the bidding phase, or is not necessary since the project’s requirement could be served by the company’s existing suite of products. If at all, minimal design changes may be needed only to configure the machine to the specific local or geophysical conditions.

This pre-manufacturing phase follows the same pattern as other manufacturing activities. The firm procures materials and services, and transports them to the manufacturing plants. Most outsourced parts and component manufacturing are usually supplied within the company group. These are then assembled either in Japan or in one of its manufacturing plants that is nearest the soon-to-be constructed power plant.

## Manufacturing of machines /construction stage and delivery

In this stage, the firm’s involvement depends on a per project basis. In some, the firm may be heavily involved in the engineering services for building projects, while in others it only needs to focus on the engineering services related to the machine manufacturing. Once the machine is ready for delivery and the power plant is ready to receive it, the firm takes care of the delivery, storage, and other logistical arrangements to bring the machine to the site of the power plant. Because of the bulkiness of these machines, the firm’s strategy has been to manufacture or assemble their products in the nearest manufacturing plant as much as possible to save on delivery cost. The parts and components, however, are procured globally from its other subsidiaries or third party suppliers. Examples of parts and components procured globally include: rotors for gas turbines, tube materials for boilers, steel plates, and cylinders. The firm may or may not install the machines themselves at the power plant site.

## Commissioning and operation of the power plant

The firm ensures that the machines are working according to specification, tests them on-site, provides the necessary personnel to install them (if asked) and train local operators. If installation services are not part of the contract, the firm, nevertheless, sends a guide to help with very sophisticated machines. Depending on the project, it may entrust the facility management and the operation of the plant to the firm. In this case, engineering services during operation are usually entrusted to the affiliated company in the relevant economy. This is why the services global network of the firm is extensive. Besides attending to after-sales services like maintenance and repair, the firm may sometimes be called upon to take responsibility for the engineering services of the entire plant facility.

Fi<sub>gu</sub>r<sub>e</sub> 10<sub>.</sub>3<sub>.</sub> Dim<sub>e</sub>n<sub>s</sub>i<sub>o</sub>n<sub>s o</sub>f th<sub>e va</sub>l<sub>ue c</sub>h<sub>a</sub>in <sub>cove</sub>r<sub>e</sub>d b<sub>y case s</sub>t<sub>u</sub>d<sub>y</sub>

## <sub>Source: APEC</sub>A<sub>.</sub> Bidd i n<sub>g</sub>

E co n o m i c/l e<sub>g</sub>a l   
<sub>re se a rc</sub> h   
S ite a sse ss m e n t   
E <sub>q</sub> u i <sub>p</sub> m e nt Des i<sub>g</sub> n   
F i n a n c i a l p roj e ct i o n s   
F e a s i b i l i t<sub>y</sub> st u d i e s   
B i d s u b m i s s i o n

## B <sub>.</sub> Pre-ma n ufactu ri n<sub>g</sub>/ <sub>p</sub>reco n st ructi o n

S u bco nt ra ct <sub>p</sub> l a nt co n st r u ct i o n <sup>\*</sup>   
P roj e ct m a n a ge m e nt <sup>\*</sup>   
P ro d u ct i o n p l a n n i ng ( i n c l u d i ng   
s <sub>u</sub> bco nt ra ct <sub>p</sub>a rts a n d   
co m po n e nt m a n u<sup>f</sup>a ct u ri ng to   
s u b s i d i a r i e s )

P roc u re m e nt of m ate ri a l s a n d <sub>p</sub> ro d u ct i o n eq u <sup>i</sup> p m e nt

Lo<sub>g</sub> i st i cs a n d c u sto m s

I n s <sub>p</sub> e ct i o n a n d t e st i n <sub>g</sub> of m a t e r i a l s

<sup>O</sup> u<sup>t</sup>so u rc <sup>i</sup> n g o<sup>f</sup> n o n - p ro p r<sup>i</sup> e<sup>t</sup>a ry p ro ce sse s

## C<sub>.</sub> Ma n ufactu ri n<sub>g</sub>/construction a nd del iver<sub>y</sub>

P roj e ct m a n a ge m e nt <sup>\*</sup>

D e l ive r<sub>y</sub> of <sub>p</sub>a rts a n d co m <sub>p</sub>o n e nts

I n - h o u se (g ro u p ) co re m a n ufa ct u ri n g a ct i v i t i e s

F i n a l a ss e m b l <sub>y</sub> i n s u bs i d i a r<sub>y</sub> n e a r powe r p <sup>l</sup> a n<sup>t</sup> o r a<sup>t</sup> powe r p <sup>l</sup> a n<sup>t</sup>

I n s <sub>p</sub> e ct i o n a n d <sub>q</sub> u a l it<sub>y</sub> co nt ro l of <sub>p</sub> ro d u cts

I n sta l l a t i o n a n d co m m i ss i o n i n <sub>g</sub> s e rv i ce s

## D<sub>.</sub> Pl a nt o<sub>p</sub>eration a nd mai ntena nce

Ce rt i fi c a t i o n <sub>p</sub> ro c e ss<sub>,</sub> o n -s i te t e st i n <sub>g</sub>

P owe r <sub>p</sub> l a nt fa c i l it<sub>y</sub> m a n a <sub>g</sub>e m e nt Re m ote m o n ito ri n<sub>g</sub>

Tra i n i n<sub>g</sub> of o <sub>p</sub>e rat i o n <sub>p</sub>e rso n n e l

M a i nte n a n ce a n d re <sub>p</sub>a i r

Note : O<sub>p</sub>tional activities in the value chain are indicated b<sub>y</sub> <sub>g</sub>reen boxes <sub>.</sub> ( <sup>\*</sup>) means <sup>‘</sup>if firm is the <sub>p</sub>rime contractor Source: APEC Policy Support Unit based on firm interview

## 10.4. Services along the Value Chain

What services activities are involved at each stage of the chosen value chain? Figure 10.4 shows a few examples of the services at each stage of the EPCM value chain. It is not an exhaustive list, and only covers the major services associated with bidding, pre-manufacturing/construction, construction, and operation of the plant<sup>5</sup>. The detailed table in Appendix A identifies at least 39 major service categories; 74 if services sub-categories of the Central Product Classification (CPC) are considered. For example, site preparation services in the construction phase can be further subdivided into demolition services, site formation and clearance services, and excavating and earthmoving services. The same goes for other major service categories like transportation services which can be either land, rail, water, or air transport services.

The firm was unable to give an estimate of the value of these services. But for the firm as a whole, the rough estimate of the current share of services in the value of the company is about one-third, while manufacturing is two-thirds. However, the services share is expected to increase due to aging of existing power plant facilities all over the world and the rising cost of building completely new facilities.

## Importance of after-sales service to the firm

In particular, the firm expects to generate more revenues from after-sales services although it acknowledges the tough competition in this market segment from other global players. Based on the after-sales services offerings on its corporate website, it appears that this segment of its business is given a high priority. The company provides detailed descriptions of various after-sales services. For example, it offers advanced inspection techniques or robotic coating of damaged tubes or parts, both for their own products as well as those of third-party supplied equipment. Just to give a flavour of the services offered in this industry, the maintenance and repair of a steam engine consists of several services – mostly engineering – such as: rotor welding and machining, blading replacement, valve inspection, repair and calibration, vibration testing and analysis, dynamic rotor balancing, and technical advisory services.

After-sales service business is defined by the firm as composed of the following: supply of parts; repair of existing parts or machines; installation services; removal of some machine parts; monitoring of operational status of customer power plants through which they can anticipate and propose repairs and maintenance needs. In some cases, the firm signs a long-term service agreement for equipment which lasts between 6 or 12 years, where the company provides the necessary manpower to carry out inspection, provides replacement parts and maintenance engineering support, trouble shoots, and monitors remotely around the clock. In addition, the firm also offers a parts supply agreement in which the firm guarantees the supply of parts for the duration of the contract at an agreed price.

## Back-office:

• Financial services

• Legal services

• IT services

## Power plant operations:

• Engineering services

• Maintenance and repair services

• Training services

## Power plant building/

## construction:

• Engineering services

• Site preparation services

• Construction services

• Certification and commissioning services

Figure 10.4. Examples of services in EPC value chain  
![](images/1f8abff70bbe3429f7c06be2416adb4aafab288a7d5d7cd41c8fdfb5b20d5204.jpg)


    ### AI Image Interpretation

    Image source: C:\Users\anugu\OneDrive\Desktop\ET-2.0-Hackathon\Backend\parsed_files\manufacturing-of-thermal-power-generation-equipment\images/1f8abff70bbe3429f7c06be2416adb4aafab288a7d5d7cd41c8fdfb5b20d5204.jpg

    The image provided appears to be a pie chart with the following information:

1. **Equipment names**:
   - Back-office
   - Power plant operations
   - Power plant building/construction
   - Bidding
   - Equipment design and power plant pre-construction/planning

2. **Equipment tags and identifiers**: 
   - Each section of the pie chart is labeled with a specific tag or identifier.

3. **Numerical values**:
   - The numerical values associated with each section are as follows:
     - Back-office: 6
     - Power plant operations: 8
     - Power plant building/construction: 18
     - Bidding: 12
     - Equipment design and power plant pre-construction/planning: 30

4. **Units**:
   - The units are not explicitly stated in the image, but they could be percentages or some other unit relevant to the context of the pie chart.

5. **Labels and annotations**:
   - Each section is labeled with a specific term related to power plant operations.
   - The sections are color-coded for visual distinction.

6. **Operational information**:
   - The pie chart seems to represent different aspects or stages in the operation of a power plant, such as bidding processes, equipment design, and operational phases.

No further details about connections between components, flow direction, electrical components, mechanical components, maintenance information, warning limits, operating limits, or specific labels for electrical diagrams are provided. The image is purely descriptive with no additional technical annotations or connections depicted.
      
Source: Compiled by APEC Policy Support Unit

## Bidding:

Research services on economic conditions, legal environment, etc.

• Land survey and site assessment services

## Equipment design and power plant pre-construction/ planning:

• Architectural services

Design services for equipment, analysis and monitoring software

Planning and management services

Procurement and logistics services

Besides repair and maintenance, other services that the firm offers are: repowering of existing facilities to raise its output and efficiency, and conversion or rehabilitation of existing machines like boilers to limit gas emissions and enhance performance. It has advanced integrity inspection technology to evaluate the deterioration of the machine from creep<sup>6</sup>, fatigue, corrosion, etc. and assess the remaining life of the machines, thereby be in the position to propose modernization and upgrading program.

## Outsourcing, bundling, and other aspects of services supply

The large scope of an EPC value chain necessitates the outsourcing of many activities. If the firm is the prime contractor, it usually subcontracts the construction of the facility to a local subcontractor who knows better the legal and regulatory environment for everything related to construction. In the subcontracting agreement, many services are typically bundled under construction services, such as staffing services, staff housing services, the acquisition of various government permits, transportation and logistics, as well as the testing of construction materials. This, in itself, is a large value chain that would merit a separate study.

In the more frequent case of the firm being only part of a consortium, its task is limited to manufacturing and delivering the machines, including installation in some cases. Once the firm has delivered, tested on-site and certified the machines, the rest depends on the plant operator, except in cases when the machines are still under warranty. Yet, even in the case where the firm is not the prime contractor, it is closely involved throughout the EPC value chain. In the bidding phase, for example, a project in-house assessment is made in terms of financial viability. Independent from the site assessment services undertaken by the prime contractor or local construction company, the firm also outsources either to a subsidiary or third party the service of assessing the topography of the plant site. The firm is sure, however, to do its own research (with help from a subsidiary or third party) on environmental and other relevant regulations in order to adjust its machines if necessary.

In the pre-manufacturing phase, the design and engineering front-end services<sup>7</sup> for the machine, the procurement services, testing and inspection, and other engineering services are all done in-house or by a subsidiary/ JV company. For IT design and software for control systems, the services may either be provided in-house or outsourced to a third party, usually an instrument and control (I&C) company. Manufacturing may take place in the different subsidiary manufacturing plants, exploiting each plant’s comparative expertise, say, in manufacturing boiler tubes, or blades, etc. These are then delivered for final assembly to the strategically chosen subsidiary that is closest to the power plant site. For example, if the power plant is being constructed in an Asian economy, the final assembly takes place in the same economy if one exists, or else in the nearest subsidiary.

Delivery and other logistical arrangements are usually outsourced to a third-party logistics provider. Installation may be undertaken by in-house personnel or by the contractor, but the certification and commissioning services as well as on-site testing are usually provided by the firm’s staff. Repairs and maintenance are done by the firm or its subsidiary, and this depends on the contract. Their machines may also be serviced by third party service providers.

In general, most of the services are carried out in-house or by the firm’s subsidiaries. Because of its extensive subsidiary network, most of the required services and materials are available within the corporate family, except for services in which the group may not have specific expertise, such as in logistics or I&C software design. Likewise, because most of the inputs are from its own subsidiaries, the trust factor on the quality of inputs and services is high, resulting in less need for strict testing and inspection, except on a random basis.

## 10.5. Policies Affecting the Value Chain

Policy discussions with the firm covered several fronts. Interestingly, on whether the policy environment determines the firm’s decision to establish in any economy, the firm said that it is not a principal determinant in the decision. Rather, more important is whether they can find a good and reliable partner in the place. In the past, establishment in various economies was part of a tariff jumping strategy because tariffs for their products were then very high.

Currently, investments in new manufacturing plant are no longer a priority because the firm thinks it has enough capacity to meet growth in the energy market in Asia and the world. Rather, more recent investments are in support or services centers, or subsidiaries with a service focus. The decision on where to locate new services subsidiaries usually depends on the number of products sold in the market, as this drives the need for more services support.

## Trade policy

The firm usually faces no major problems with customs because their products are specialized machines. But uncertainty about whether or not its imports will be accorded a preferential tariff obliges them to assume in their bid that the highest tariff will be payable. This makes the cost of the project (and their bid price) higher than if they knew for certain beforehand what tariff rate will be used. Ultimately, the higher cost occasioned by this uncertainty is borne by the customer (the utility) and eventually by the end-users. Clear guidelines and agreement on tariffs and other relevant policies at the outset would be helpful in lessening the cost of the project.

## Human capital needs

A major concern is the large employee turnover, especially of engineers, in their subsidiaries in developing economies. This is related to the small pool of quality engineers relative to those in developed economies. In turn, this is connected to the quality of education in the respective host markets. The firm’s strategy is to train local talent in order to minimize the need to use many Japanese expatriates which costs the company more. But the firm also sees the need for different Asian economies to upgrade their education and skills development. Human capital development and skills matching is important to support large manufacturing and service facilities that are set up in the economy.

## Labour mobility

To support their customers, sometimes it is necessary to dispatch engineers from Japan or elsewhere in less than 24 hours to prevent a plant shutdown<sup>8</sup>. But in some economies with visa restrictions, it takes time to send the necessary personnel. Though the application process in itself is not difficult for the firm, it is still time consuming, and delays can become costly. The firm thinks that minimizing the visa processing period would greatly help, particularly for very short-term and temporary stays of intracorporate transferees.

Other labour-related regulations that pose a threat are indirect regulations on corporate officers’ qualifications. For example, in one Asian economy, a regulation being discussed in its legislative assembly is the language test requirement for managers and directors. If approved, this requirement effectively puts restrictions on foreign directors, putting unnecessary burden on them in carrying out their responsibilities.

Services provided by foreign personnel, such as the installation and commissioning of machinery or to act as EPC project technical advisor, are usually subject to a withholding tax if the personnel stays beyond a certain threshold number of days, which in some economies is up to 60 days. The additional cost incurred is something that the firm takes as a given. But in some economies, particularly in those where Japan has no bilateral agreement on double taxation, the withholding tax can go beyond the fees for technical services and also include a tax on royalties.

## Intellectual property

Some economies require the local transfer of intellectual property (IP), whether for imported components or for manufacturing. The firm has resolved the potential difficulty arising from such a regulation by forming a joint venture to which it licenses the IP with restricted conditions, i.e. only for the purpose of manufacturing for the specific market (exclusive market)<sup>9</sup>. The joint venture receives all the drawings and technical designs but must ensure no leakage of the IP. Any improvement work on the licensed IP, however, will belong to the joint venture.

So far, the arrangement appears satisfactory. The firm is, however, aware that other companies have experienced either leakage in the use of their IP or non-observance of the restrictions on IP use by their local partner. In particular, these companies found machines being sold in other Asian economies that made use of their licensed technology when its use is supposed to be restricted to one particular economy in Asia. Improved IP protection and the implementation of rules in different economies, as well as the careful choice of local partners, are important to safeguard corporate intellectual property.

## Equity limitation

As a rule, the firm prefers to be free to decide whether to acquire local partners, i.e. have a fully-owned subsidiary, or form a joint venture. This decision is made on a case-by-case basis. In some places acquisition is the best way to enter the market. In certain economies, however, there is preference for joint ventures or even an expectation that these will be established. The vehicle for ensuring that this occurs is rules on foreign equity shares. In some cases where the firm finds a good local partner, it does not consider foreign equity limits an operational constraint. This view is clearest with respect to manufacturing, but less so with after-sales services. The reason for this is that the firm considers that its reputation, and possibly its IP, is at greater risk in this market segment<sup>10</sup>.

Though there has been a relaxation of equity restrictions in some economies in the case of the energy industry, restrictions still abound in construction services. Some of these restrictions include permits or licenses to become a contractor, with specified conditions on how to obtain such licenses for example, years of engineering experience, education, etc. If licensing for the engineering profession is restrictive, establishing a foreign-owned construction company in the economy concerned becomes virtually impossible. Restrictions like this in construction services affect the firm’s capacity to lead consortia as the prime contractor in particular economies.

## Local content requirements

The firm feels that there is need for clear guidelines on local content requirements. It noted that in some projects in the region, the local content requirement is too high and detailed rules on its computations are not very clear. It is particularly problematic especially if there are not enough companies in the host economy that can satisfy the stringent technical requirement by the firm for power plant construction projects. In some cases, it is virtually impossible to meet the local content requirement.

## Health, safety and environment regulations

To ensure compliance with government regulations on health, safety, and environment, there is a need for government to visit and inspect facilities. However, overly frequent visits add unnecessarily to firm costs, particularly because the inspectors’ costs of transportation, accommodation, and other expenses are usually borne by the power plant management. For large enterprises, these costs may be negligible. But if an independent power provider - the firm’s customer - is small, it will try to recoup these additional costs either through hard bargaining with the equipment provider and other suppliers on price, or pass the cost on to final end-users of electricity.

## Transparency

The energy generation business has to deal with various government regulations, for example on environmental issues, land ownership, permits, and various taxes. But in many economies, information is difficult to obtain and the firm has to rely on local companies to get the information.

Likewise, when there are delays in plant construction, the firm has often felt that it is left unaware of the project status and of the difficulties that arise in the implementation process<sup>11</sup>. Since the firm bases its manufacturing schedule on the plant construction schedule, delays in project implementation have a huge impact on cost. For example, the firm might have finished manufacturing the bespoke equipment for a project and if the plant is not yet ready, it incurs storage and maintenance costs. If the firm delay the manufacture of particular types of equipment for a specific power plant, the delay cascades down on all their suppliers as well as on the schedules of the different subsidiaries that may be involved in supplying parts for the equipment. Most of the factors causing delay are difficult for foreign firms to observe or anticipate, particularly if the government is not transparent.

The risk of delays and other similar risks that are frequently prevalent in developing economies are typically factored into project costs, but only to a limited degree because of competition from other bidding consortia. In sum, for big infrastructure projects like power plants, a government’s capacity to implement the project according to agreed timelines can minimize overall cost and thus ultimately improve the provision of electricity at a cheaper cost.

## A<sub>ppe</sub>ndi<sub>x</sub> A

List of <sub>p</sub>otential ser<sub>v</sub>ices for desi<sub>g</sub>nin<sub>g</sub> b<sub>u</sub>ildin<sub>g</sub> and o<sub>p</sub>eratin<sub>g</sub> a <sub>p</sub>o<sub>w</sub>er <sub>p</sub>lant

T<sub>a</sub>bl<sub>e</sub> A<sub>.</sub> 1<sub>.</sub> S<sub>e</sub>r<sub>v</sub>i<sub>ces</sub> d<sub>u</sub>rin<sub>g</sub> biddin<sub>g</sub> <sub>s</sub>t<sub>age</sub>
<table><tr><td colspan="2" rowspan="1">Service</td><td colspan="1" rowspan="1">Corresponding CPC Ver. 2 Code</td><td colspan="1" rowspan="1">Supplied in-house</td><td colspan="1" rowspan="1">Outsourced to affiliatedcompanies andreasons12</td><td colspan="1" rowspan="1">Outsourced to third-party suppliers andreasons</td><td colspan="6" rowspan="1">Remarks</td></tr><tr><td colspan="1" rowspan="2">1</td><td colspan="1" rowspan="2">Research oneconomic conditions,legal environment,etc. on economywhere power plantwill be built</td><td colspan="1" rowspan="1">81212 – Research and developmentservices in economics</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td><td colspan="6" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">81213 – Research and developmentservices in law</td><td colspan="1" rowspan="1">Yes if primecontractor; or elseNo</td><td colspan="1" rowspan="1">Yes if prime contractor;or else No</td><td colspan="1" rowspan="1"></td><td colspan="6" rowspan="1"></td></tr><tr><td colspan="1" rowspan="5">2</td><td colspan="1" rowspan="5">Land survey;site assessmentservices</td><td colspan="1" rowspan="1">83411 – Geological and geophysicalconsulting services</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes, proximity</td><td colspan="1" rowspan="1">Yes</td><td colspan="6" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83412 – Geophysical services</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes , proximity</td><td colspan="1" rowspan="1">Yes</td><td colspan="6" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83421 – Surface surveying services</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes , proximity</td><td colspan="1" rowspan="1">Yes</td><td colspan="6" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83442 – Testing and analysisservices of physical properties</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes, proximity</td><td colspan="1" rowspan="1">Yes</td><td colspan="6" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="6" rowspan="1"></td></tr><tr><td colspan="7" rowspan="3">3 Back-office services                                                                              Yes(e.g. feasibility study,project bid                                                              Yespreparation)</td></tr><tr><td colspan="1" rowspan="1">Preparation of bidding document</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Headquarter services</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">Design services</td><td colspan="1" rowspan="1">83912 – Industrial design services</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">If necessary toadjust existingdesign to localconditions</td></tr><tr><td colspan="1" rowspan="2">5</td><td colspan="1" rowspan="2">Telecommunicationservices</td><td colspan="1" rowspan="1">CPC 841: Telephony and othertelecommunication services</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes, needseconomies of scale</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">CPC 842: Internettelecommunication services</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes, needseconomies of scale</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">Planning andmanagement services</td><td colspan="1" rowspan="1">Selection of contractors for facilityconstruction</td><td colspan="1" rowspan="1">Yes if primecontractor</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr></table>

Table A<sub>.</sub>2<sub>.</sub> Ser<sub>v</sub>ices d<sub>u</sub>rin<sub>g</sub> desi<sub>g</sub>n sta<sub>g</sub>e of e<sub>qu</sub>i<sub>p</sub>ment and <sub>p</sub>re<sub>-</sub>constr<sub>u</sub>ction/<sub>p</sub>lannin<sub>g</sub> sta<sub>g</sub>e of <sub>p</sub>o<sub>w</sub>er <sub>p</sub>lant
<table><tr><td colspan="2" rowspan="1">Service</td><td colspan="1" rowspan="1">Corresponding CPC Ver. 2 Code</td><td colspan="1" rowspan="1">Supplied in-house</td><td colspan="1" rowspan="1">Outsourced toaffiliated companiesand reasons14</td><td colspan="1" rowspan="1">Outsourced to third-party suppliers andreasons</td><td colspan="1" rowspan="1">Bundled</td></tr><tr><td colspan="1" rowspan="4">7</td><td colspan="1" rowspan="4">Site assessmentservices</td><td colspan="1" rowspan="1">83411 – Geological andgeophysical consulting services</td><td colspan="1" rowspan="1">Yes, if primecontractor</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes 15; use of outsideexpertise</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83412 – Geophysical services</td><td colspan="1" rowspan="1">Yes, if primecontractor</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes; use of outsideexpertise</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83421 – Surface surveyingservices</td><td colspan="1" rowspan="1">Yes, if primecontractor</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes; use of outsideexpertise</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83442 – Testing and analysisservices of physical properties</td><td colspan="1" rowspan="1">Yes, if primecontractor</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes; use of outsideexpertise</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">8</td><td colspan="1" rowspan="2">Architecturalservices for powerplant building</td><td colspan="1" rowspan="1">8321 – Architectural services andadvisory services</td><td colspan="1" rowspan="1">Depends onproject</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes to constructionservices company;engineering company;lack of in-houseexpertise</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">8323 – Landscape architecturalservices and advisory services</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes to constructionservices company;engineering company;lack of in-houseexpertise</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="2" rowspan="5">9  Design services forequipment as wellas analysis andmonitoringsoftware</td><td colspan="1" rowspan="1">83912 – Industrial design services</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">If necessary todesign a new one;or else adjustexisting ones.</td></tr><tr><td colspan="1" rowspan="1">8392 – Design originals; originaldesign concepts, produced onown account:· industrial product designs·aesthetic designs·graphic designs</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">If necessary todesign a new one;or else adjustexisting ones.</td></tr><tr><td colspan="1" rowspan="1">83141 - IT design anddevelopment services forapplications</td><td colspan="1" rowspan="1">Depends onproject;Yes (dependson project andeconomy)</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes, to Instrumentaland Control (I&amp;C)Company; lack ofexpertise</td><td colspan="1" rowspan="1">Simple controldesign requirementfrom economiesmay be done in-house</td></tr><tr><td colspan="1" rowspan="1">83142 – IT design anddevelopment services fornetworks and systems</td><td colspan="1" rowspan="1">Depends onproject;Yes (dependson project andeconomy</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes, to Instrumentaland Control (I&amp;C)Company; lack ofexpertise</td><td colspan="1" rowspan="1">Simple controldesign requirementfrom economiesmay be done in-house</td></tr><tr><td colspan="1" rowspan="1">83143 – Software originals -copyrighted intellectual propertyproduced without contract foroutright sale</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes; lack of expertise</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">Government-related pre-building services(e.g. securing</td><td colspan="1" rowspan="1">91132 - Public administrativeservices related to fuel andenergy</td><td colspan="1" rowspan="1">Primecontractor</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes, for efficiency</td><td colspan="1" rowspan="1">Usually bundledwith constructionservices</td></tr><tr><td colspan="1" rowspan="2"></td><td colspan="1" rowspan="2">governmentpermits forconstruction)</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">91133 - Public administrativeservices related to mining andmineral resources, manufacturingand construction</td><td colspan="1" rowspan="1">Primecontractor;Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes, for efficiency</td><td colspan="1" rowspan="1">Usually bundledwith constructionservices</td></tr><tr><td colspan="1" rowspan="5">11</td><td colspan="1" rowspan="5">Planning andmanagementservices</td><td colspan="1" rowspan="1">83223 – Project site masterplanning services</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83330 – Project managementservices for construction projects</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes, constructioncompany/ engineeringcompany; efficiencyconsiderations</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Selection of contractors for facilityconstruction</td><td colspan="1" rowspan="1">Yes if primecontractor</td><td colspan="1" rowspan="1">Yes if prime contractor</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83190 – Other managementservices, except constructionproject management services(Selection of contractors forarchitectural design)</td><td colspan="1" rowspan="1">Yes if primecontractor</td><td colspan="1" rowspan="1">Yes if prime contractor</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83190 – Other managementservices, except constructionproject management services(Selection of contractors forengineering design)</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">Constructionservices</td><td colspan="1" rowspan="1">CPC 54: Construction services</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes if prime contractor</td><td colspan="1" rowspan="1">Yes; outside expertise</td><td colspan="1" rowspan="1">*Bundled withconstructionmaterials, leasingof equipment,</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">labor supply as wellas accompanyingcomponents suchas housing,medical, insurance,etc.</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">Research anddevelopmentservices</td><td colspan="1" rowspan="1">8112 – Research and experimentaldevelopment services inengineering &amp; technology</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes; simple engineeringor adjustments tomachines</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">14</td><td colspan="1" rowspan="2">Procurementservices</td><td colspan="1" rowspan="1">83116 – Supply chain and othermanagement consulting services</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">85999 – Other support servicesn.e.c.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">15</td><td colspan="1" rowspan="2">Customs clearanceservices andlogistics of rawmaterials</td><td colspan="1" rowspan="1">67110 – Container handlingservices</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes; outside expertise</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">85999 – Other support servicesn.e.c. (business brokerage)</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">Technical testingof raw materials</td><td colspan="1" rowspan="1">83441 – Composition and puritytesting and analysis services</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="4">17</td><td colspan="1" rowspan="4">Transport servicesof raw materials</td><td colspan="1" rowspan="1">651 – Land transport services offreight</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes; efficiency</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">652 – Water transport services offreight</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes; efficiency</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">6531 – Air transport services offreight</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes; fficiency</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">67910 – Freight transport agencyservices and other freighttransport services</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes; efficiency</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">Environmentalconsulting services</td><td colspan="1" rowspan="1">83931 – Environmental consultingservices</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes; lack of expertise</td><td colspan="1" rowspan="1"></td></tr></table>

T<sub>a</sub>bl<sub>e</sub> A<sub>.</sub>3<sub>.</sub> S<sub>e</sub>r<sub>v</sub>i<sub>ces</sub> d<sub>u</sub>rin<sub>g</sub> b<sub>u</sub>ildin<sub>g</sub>/<sub>co</sub>n<sub>s</sub>tr<sub>uc</sub>ti<sub>o</sub>n <sub>s</sub>t<sub>age o</sub>f <sub>powe</sub>r <sub>p</sub>l<sub>a</sub>nt
<table><tr><td colspan="2" rowspan="1">Service</td><td colspan="1" rowspan="1">Corresponding CPC Ver. 2 Code</td><td colspan="1" rowspan="1">Supplied in-house</td><td colspan="1" rowspan="1">Outsourced to affiliatedcompanies and reasons</td><td colspan="1" rowspan="1">Outsourced to third-party suppliers andreasons</td><td colspan="1" rowspan="1">Bundled</td></tr><tr><td colspan="1" rowspan="3">19</td><td colspan="1" rowspan="3">Engineering servicesduringbuilding/construction</td><td colspan="1" rowspan="1">83310 – Engineering advisoryservices</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83321 – Engineering services forbuilding projects</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Construction /engineeringcompany; due toeconomies of scale</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">83324 – Engineering services forpower projects</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="3">20</td><td colspan="1" rowspan="3">Site preparationservices</td><td colspan="1" rowspan="1">54310 – Demolition services</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">54320 – Site formation andclearance services</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">54330 – Excavating andearthmoving services</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">Importation of powerplant equipment:Customs clearance andlogistics</td><td colspan="1" rowspan="1">85999 – Other support servicesn.e.c.</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">22</td><td colspan="1" rowspan="2">Importation of powerplant equipment:Freight transportationservices</td><td colspan="1" rowspan="1">6511 – Road transport servicesof freight</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">6512 – Rail transport services offreight</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2"></td><td colspan="1" rowspan="2"></td><td colspan="1" rowspan="1">652 – Water transport servicesof freight</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">653 – Air and space transportservices of freight</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">23</td><td colspan="1" rowspan="2">Importation of powerplant equipment:Storage andwarehousing services</td><td colspan="1" rowspan="1">67220 – Bulk liquid or gasstorage services</td><td colspan="1" rowspan="1">Primecontractor</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">67290 – Other storage andwarehousing services</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes; proximity</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">Construction services</td><td colspan="1" rowspan="1">54 – Construction services</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Construction/engineeringcompany</td><td colspan="1" rowspan="1">*Bundled withconstructionmaterials, leasingof equipment,labor supply as wellas accompanyingcomponents suchas housing,medical, insurance,etc.</td></tr><tr><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">Installation services forequipment and relatedcomponents such aswiring</td><td colspan="1" rowspan="1">546 – Installation services</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Construction/engineeringcompany</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">26</td><td colspan="1" rowspan="1">Certification andcommissioning servicesof power plant buildingand equipment by firm</td><td colspan="1" rowspan="1">8344 – Technical testing andanalysis services</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">27</td><td colspan="1" rowspan="1">Governmentinspections on fireprevention, healthhazards, environmental</td><td colspan="1" rowspan="1">91132 – Public administrativeservices related to fuel andenergy</td><td colspan="1" rowspan="1">Project basis</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Yes; required by law</td><td colspan="1" rowspan="1"></td></tr></table>

<table><tr><td>aspects</td><td>protection and other</td><td>9129 – Public administrative services related to other public order and safety affairs</td><td>Project basis</td><td>Yes; required by law</td><td></td></tr></table>

T<sub>a</sub>bl<sub>e</sub> A<sub>.</sub>4<sub>.</sub> S<sub>e</sub>r<sub>v</sub>i<sub>ces</sub> d<sub>u</sub>rin<sub>g ope</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s s</sub>t<sub>age o</sub>f <sub>powe</sub>r <sub>p</sub>l<sub>a</sub>nt
<table><tr><td rowspan=1 colspan=2>Service</td><td rowspan=1 colspan=1>Corresponding CPC Ver. 2 Code</td><td rowspan=1 colspan=1>Supplied in-house</td><td rowspan=1 colspan=1>Outsourced to affiliatedcompanies and reasons</td><td rowspan=1 colspan=1>Outsourced to third-party suppliers andreasons</td><td rowspan=1 colspan=1>Bundled</td></tr><tr><td rowspan=2 colspan=1>28</td><td rowspan=2 colspan=1>Engineering services duringoperations</td><td rowspan=1 colspan=1>83310 – Engineering advisoryservices</td><td rowspan=1 colspan=1>Project basis</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>83324 – Engineering servicesfor power projects</td><td rowspan=1 colspan=1>Yes (if part ofcontract)</td><td rowspan=1 colspan=1>Yes (if part of contract);to affiliated companiesin relevant economy</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>29</td><td rowspan=2 colspan=1>Information technology (IT)services for on-site andremote monitoring ofpower plant</td><td rowspan=1 colspan=1>8315 – Hosting and informationtechnology (IT) infrastructureprovisioning services</td><td rowspan=1 colspan=1>Yes (if part ofcontract)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>8316 – IT infrastructure andnetwork management services</td><td rowspan=1 colspan=1>Yes (if part ofcontract)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>Telephone-based supportservices</td><td rowspan=1 colspan=1>85931 – Telephone call centreservices</td><td rowspan=1 colspan=1>Yes (if part ofcontract)</td><td rowspan=1 colspan=1>Yes (if part of contract);to affiliated companiesin relevant economy</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>Diagnostic, inspection,maintenance and repair ofequipment</td><td rowspan=1 colspan=1>87156 – Maintenance andrepair services of commercialand industrial machinery</td><td rowspan=1 colspan=1>Yes (if part ofcontract)</td><td rowspan=1 colspan=1>Yes (if part of contract);to affiliated companiesin relevant economy</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>Installation services forreplacement parts andequipment as well asrelated components such aswiring</td><td rowspan=1 colspan=1>546 – Installation services</td><td rowspan=1 colspan=1>Yes (ifordered)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>33</td><td rowspan=1 colspan=1>Training services forworkers</td><td rowspan=1 colspan=1>9291 – Other education andtraining services</td><td rowspan=1 colspan=1>Project basis</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

Table A<sub>.</sub>5<sub>.</sub> Back-office services (before durin<sub>g</sub> and after plant construction)
<table><tr><td rowspan=1 colspan=2>Service</td><td rowspan=1 colspan=1>Corresponding CPC Ver. 2Code</td><td rowspan=1 colspan=1>Supplied in-house</td><td rowspan=1 colspan=1>Outsourced to affiliatedcompanies and reasons</td><td rowspan=1 colspan=1>Outsourced to third-party suppliers andreasons</td><td rowspan=1 colspan=1>Bundled</td></tr><tr><td rowspan=1 colspan=1>34</td><td rowspan=1 colspan=1>Financial services</td><td rowspan=1 colspan=1>71 – Financial and relatedservices</td><td rowspan=1 colspan=1>Yes if primecontractor</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Yes; economies ofscale</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>Insurance services</td><td rowspan=1 colspan=1>713 - Insurance and pensionservices</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Yes; economies ofscale</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>Accounting, auditing andbookkeeping services</td><td rowspan=1 colspan=1>822 – Accounting, auditingand bookkeeping services</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Yes; required by law</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>37</td><td rowspan=1 colspan=1>Legal services</td><td rowspan=1 colspan=1>821 – Legal services</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Yes; lack of in-houseexpertise</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>Information technologyservices</td><td rowspan=1 colspan=1>8313 – Informationtechnology (IT) consulting andsupport services</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Yes; economies ofscale</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>39</td><td rowspan=1 colspan=1>Visa and immigrationservices for foreignemployees</td><td rowspan=1 colspan=1>91290 – Public administrativeservices related to otherpublic order and safety affairs</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Yes; efficiency</td><td rowspan=1 colspan=1></td></tr></table>

S<sub>ource:</sub> C<sub>omp</sub>il<sub>e</sub>d b<sub>y</sub> APEC P<sub>o</sub>li<sub>cy</sub> S<sub>uppor</sub>t U<sub>n</sub>it