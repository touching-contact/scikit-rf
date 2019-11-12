# Purpose

De-embedding Program Set-up

# Progress

## 1. choosing base program

 RF & Microwave Engineering Toolkit   coded by python

https://github.com/scikit-rf/scikit-rf

## 2. related environment setup

- Python3.0
- Git :  a distributed version control system 
- Anaconda :  *The industry standard for open-source data science* 
- Atom : A hackable text editor
- Typora : markdown editor ( you can read better this document by Typora  )

## 3. studying scikit-rf

- plotting  practice : \scikit-rf\examples\basic_touchstone_plotting
- manual reading  :  \scikit-rf\doc\source\tutorials\Introduction.ipynb
- manual reading  : \scikit-rf\doc\source\tutorials\Networks.ipynb
- de-embedding practice : \scikit-rf\examples\test.py , \scikit-rf\examples\de-embedding\de-embedding_test.py

## 4. de-embedding Measurement Data 

### measurement data : 

- \scikit-rf\examples\de-embedding\E_PROBE_THROUGH.S2P
- \scikit-rf\examples\de-embedding\Inductor_0p6nH.s2p

### trying :

- \scikit-rf\examples\de-embedding\probe.py  with original data

  fail because frequency data does not have same format

- \scikit-rf\examples\de-embedding\probe.py  with modified data

​       fail because frequency data does not have same significant numbers ( refer following tail part of each data file )

`\scikit-rf\examples\de-embedding\probe.freq`

`14.881180362 0.4908555528213796 0.23567564462556162 -0.33197324454122 0.39569762464936176 -0.3296960735524074 0.3969671548412763 0.30817230912448207 0.36880860340590554`
`14.920786908 0.5109262982995203 0.12474050117162366 -0.23966634284347357 0.4597813351742145 -0.23921244277432502 0.46027376983517565 0.3802650378713404 0.29076076136034174`
`14.960393454 0.5202553432377257 0.001088588508351484 -0.13120868577407677 0.503743132763353 -0.1313730302090057 0.5038585025703666 0.4390865790126726 0.2026051428207211`
`15.0`

`\scikit-rf\examples\de-embedding\inductor.freq`

`14.8812 0.23938684189016995 0.42670971544614333 0.7606135030597303 -0.4267089728812819 0.7606135030597303 -0.4267089728812819 0.23938684189016995 0.42670971544614333`
`14.9208 0.24035667361956828 0.4272999422693778 0.7596435140878796 -0.4273002875056257 0.7596435140878796 -0.4273002875056257 0.24035667361956828 0.4272999422693778`
`14.9604 0.24132569975958787 0.4278876523343307 0.758674092947713 -0.4278869824152386 0.758674092947713 -0.4278869824152386 0.24132569975958787 0.4278876523343307`
`15.0`

### holding  at 2019.11.11

