# joint-pitching-analysis-MASL

Github repository for the MASL to use when processing captured motion data and analysing musculoskeletal activity. This repository will hopefully serve as a more accessible way to access OpenSim's features by doing a majority of the preprocessing work & scripting in the OpenSim software for those less familiar with programming. Please note that this repository is based on the usage of OpenBiomechanic's baseball pitching database [link here](https://github.com/drivelineresearch/openbiomechanics/tree/main/baseball_pitching). Revisions will be made so that the scripts used here are adaptable to c3d data from any motion database.

Key features include:
- python scripts handling the conversion of csv data into .trc files and .mot files usable by the OpenSim software in [csvtotrc.py](/processing scripts/csvtotrc.py)
- TODO: python scripts handling the marker assignment (.XML) and scaling of the model selected.
- TODO: automated python script handling high throughput data analysis to automate a selected pipeline in OpenSim.

Future updates/todos include:
- Include simple user interface (tkinter) so that users do not have to directly edit the code.
- Write c3d to .trc/.mot conversion using the python ezc3d library.
