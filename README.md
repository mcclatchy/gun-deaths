# Since Parkland

This was a project between [McClatchy](https://www.mcclatchydc.com/), the [Miami Herald](https://www.miamiherald.com) and [The Trace](https://www.thetrace.org), a nonprofit news organization reporting on guns, to document youth gun-involved deaths in the 12 months since the Feb. 14, 2018, Parkland High School Shooting.

The organizations pulled information on gun-involved deaths of school-age children from the nonprofit research group [Gun Violence Archive](https://www.gunviolencearchive.org), which culls reports of gun-involved incidents from more than 2,000 media sources. To compare deaths in the year since Parkland to those before, McClatchy classified each year as starting on Feb. 14 and ending on Feb. 13.

To confirm the data and fill in missing details, McClatchy requested incident reports for each of the deaths from the police agencies that investigated each case. To do this, McClatchy compiled a database of law enforcement media and records contacts for more than 600 agencies and wrote a program to send records requests to each agency.

Data for the year since Parkland are in `data.csv`.

Data for the four years before Parkland are in `historicalData.csv`.

The Python script to automate records requests is `requestSender.py`. The script uses Google's API to run down a list of incidents in a Google sheet and write templated records requests to more than 650 police agencies. McClatchy compiled this database for the purposes of fact-checking information from Gun Violence Archive and adding new information where able.

More can be read on the methodology [here](https://www.miamiherald.com/news/nation-world/national/article224957145.html). Stories can be read here. Obits on almost all of the children can be found here.

## Questions

Contact Caitlin Ostroff at costroff@mcclatchydc.com.
