# eicview

Overview
--------
Different links of artifacts objects

**Detector geometry viewer:**
- [Central detector](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/detector_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom120;ROTY320;ROTZ340;trz0;trr0;ctrl;all)
- [Full Detector (including beamline)](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/detector_geo_full.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom75;ROTY290;ROTZ350;trz0;trr0;ctrl;all)
- [Inner detector (without calorimetry)](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/inner_detector_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom75;ROTY320;ROTZ340;trz0;trr0;ctrl;all)
- Subsystem views:
  - [Calorimetry](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/calorimeters_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom120;ROTY320;ROTZ340;trz0;trr0;ctrl;all)
  - [PID](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/pid_only_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom75;ROTY320;ROTZ340;trz0;trr0;ctrl;all)
    - [dRICH](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/drich_only_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom75;ROTY290;ROTZ350;trz0;trr0;ctrl;all)
    - [pfRICH](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/pfrich_only_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom55;ROTY49;ROTZ350;trz0;trr0;ctrl;all&)
    - [DIRC](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/dirc_only_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom120;ROTY320;ROTZ340;trz0;trr0;ctrl;all)
    - [ToF](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/tof_only_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom55;ROTY49;ROTZ350;trz0;trr0;ctrl;all&)
  - [Tracking](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/tracking_only_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom75;ROTY320;ROTZ340;trz0;trr0;ctrl;all)
    - [Vertex detector](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/vertex_only_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom120;ROTY320;ROTZ340;trz0;trr0;ctrl;all)
  - [Far-forward](https://eic.phy.anl.gov/geoviewer/index.htm?nobrowser&file=https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/geo/ip6_geo.root?job=dump_geometry&item=default;1&opt=clipx;clipy;transp30;zoom40;ROTY290;ROTZ350;trz0;trr0;ctrl;all)

<a href="https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/images/view01.pdf?job=report">
<img src="https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/images/view01.png?job=report" width="400px" />
</a>

<br />
<a href="https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/images/view01_top.pdf?job=report">
<img src="https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/images/view01_top.png?job=report" width="400px" />
</a>

[Browse latest](https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/browse/images?job=report)

[Detector views](https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/doc/dawn_views.md?job=report)

[Constants listing](https://eicweb.phy.anl.gov/EIC/detectors/athena/-/jobs/artifacts/master/raw/doc/constants.out?job=report)


## Python backend

Install everything

```
cd backend
pip install -r requirements.txt
```

[python-gitlab library documentation](https://python-gitlab.readthedocs.io/en/stable/)
[pagination](https://python-gitlab.readthedocs.io/en/stable/api-usage.html?highlight=per_page#pagination)

## GitLab API

[Pagination](https://docs.gitlab.com/ee/api/#pagination)

[Download artifacts](https://docs.gitlab.com/ee/api/job_artifacts.html)