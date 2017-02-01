# Semiconductor Fabrication Process

## Contents

* Semiconductor Wafer Process
  - Lithography
  - Etch
  - Diffusion
  - Thin Film
  - Capacitor
  - CMP & Cleaning

* Semiconductor Wafer Integration Process
  - Isolation
  - Word Line
  - Landing Pad Contact
  - Bit Line
  - Storage Node Contact
  - Capacitor
  - MLM
  
  * Semiconductor Wafer Failure Anaylsis
 
 ## Lithography
 
 * Coating (Eqipment: Track)
 * Exposure (Stepper)
 * PEB (Track)
 * Wet Develop (Track)
 * Substrate Etching (Track)
 
 ## Etch
 
 * Wet Etching (by Wet chemical solution: Isotropic Etching)

  - Vertical E/R = Horizontal E/R
  - Pure Chemical Reaction
  - High Selectivity
  - CD Loss or Gain
  - High Pressure
  - Batch Wafer Type
  - Less Electrical Damage


 * Dry Etching (by Plasma: Anisotropic Etching)

  - Vertical E/R >> Horizontal E/R
  - Ion assisted
  - Relatively low Selectivity
  - No CD bias
  - Low Pressure
  - High Directionality
  - Single Wafer Type
  - Low Etch rate
  - Purely Physical Process

 
 ## Diffusion
 
 * Junction(Diffusion) : inject Dopant into junction of Si(wafer) + Heat processing = diffusion(Annealing)  in Si(wafer)
 * Oxidation : O2, H2O
 * CVD(Chemical Vapor Deposition) : SiH2Cl2 & NH3
 
 ## Capacitor(measured by Capacitance) : ILD-MLM, Cap Oxide, LPC-B/L & BLC, HM-W/L, ISO
 
 ## Thin Film
 
 requirement:
> Smooth surface
> High etch by products vapor pressure
> Not Oxidize, stable oxide
> Good adhesion, low stress
> No reacted with cleaning chemical: HCl, NH4OH, H2O2, HF
> Resistant to high current density & stress
> High stablity with Heat : for gate, bit line
 
* Layer
 Diffusion Barrier
 Signal / Power line
 Planarization
 Etch Barrier
 Gap-fill
 Word line / Bit line / Contact
 
 ## CMP
 
 ess – CMP
1. Shallow Trench Isolation CMP
2. Inter Level Dielectric CMP
3. Inter Metal Dielectric CMP
4. Plug poly CMP
5. Plug isolation(Modified SAC)
6. W plug/via formation
7. Al or Cu Damascene
8. X-tal silicon polishing (SOI)
9. Noble Metal(Pt/Ru/Ir/IrO2/TiAl/N/RTN/RTO 등)
10. Damascene Gate

## Cleaning


---

# Process Flow Design (in Process Integration)
* Photo
* Etch
* Diffusion
* Thin Film
* Ion Implantation
* CMP/Cleaning


## Isolation

For separating Actives from other Actives: Make ISO


- Conventional LOCOS (Local Oxidation of Silicon)
- PBL (Poly Buffered LOCOS)
- STI (Shallow Trench Isolation)

Sequence:
• Pad Ox.
• Pad Nit DEP
• ISO Mask(1)
• ISO Etch
• ISO PR strip & PET
• Wall Ox.
• ISO HDP DEP
• STI CMP
• ISO Nit Strip
• Well Formation

## Word Line

for developing(building) Transistor electrode(Gate) : develop WL over ISO

Sequence:
• Gate Oxidation
• Gate Poly DEP
• Gate Metal DEP
• Gate HM DEP
• Gate Mask
• Gate Etch
• LDD Formation
• Gate Spacer DEP

## Contact
(bridge process)
for connecting 'S/D junction' of the cell transistors to 'Bit Line' & 'Storage Node Contact' : build PC over WL

- Use Self-Aligned Contact

Sequence:
• ILD DEP
• Gate Spacer etch
• Spacer SiN Dep
• ILD Dep
• ILD CMP
• LPC Mask
• LPC etch/PRST
• Poly Dep
• Poly CMP


## Bit Line

for building 'current path' between 'drain area' of the transistors and 'outer circuit' : build BL & BLC1 over WL

Sequence:
• ILD DEP
• BLC Mask
• BLC etch
• BLC Mask
• BLC etch
• BL DEP
• BL HM DEP
• BL Mask
• BL Etch


## Node Contact

for building 'contact' connecting 'LPC1' to 'Storage Node' : build C

Sequence:
• ILD HDP DEP
• ILD CMP
• C Mask
• C etch
• C Poly DEP
• C Poly EB (or CMP)


## Capacitor

for building 'cell capacitor', which contains informations : build CAP

Sequence:
• Storage node oxide DEP
• CAP Mask
• SN oxide etch
• SN DEP
• SN PR coating
• SN EB (or CMP)
• SN PR Strip
• Capacitor dielectric film DEP
• Plate DEP
• Plate Mask
• Plate Etch

## MLM

for build 'Metal Line' used to connect for each or the outer, and to supply the power : build Metal & MC

Sequence:
• ILD DEP
• ILD CMP
• MC Mask
• MC etch
• MC DEP
• MC Etch back(or W Plug CMP)
• M DEP
• M Mask
• M Etch
• IMD DEP
• IMD CMP
• MC Mask
• MC etch
• MC DEP
• MC Etch back
• M Al DEP
• M Mask
• M etch
• Passivation
• PAD Mask
• Repair-etch
• Anneal


BL-LP2(SNC)
