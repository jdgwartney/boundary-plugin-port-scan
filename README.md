# Boundary Port Scan Plugin

Measures the time to establish a connection on a TCP/IP port of a host.

### Prerequisites

|     OS    | Linux | Windows | SmartOS | OS X |
|:----------|:-----:|:-------:|:-------:|:----:|
| Supported |   v   |    v    |    v    |  v   |

#### For Boundary Meter v4.2 or later

- To install new meter go to Settings->Installation or [see instructions](https://help.boundary.com/hc/en-us/sections/200634331-Installation).
- To upgrade the meter to the latest version - [see instructions](https://help.boundary.com/hc/en-us/articles/201573102-Upgrading-the-Boundary-Meter). 

### Plugin Setup

None

### Plugin Configuration Fields

|Field Name  |Description                                            |
|:-----------|:------------------------------------------------------|
|Source      |The source to display in the legend for the time data. |
|Port        |The redis port.                                        |
|Host        |The redis hostname.                                    |
|PollInterval|Interval (in milliseconds) to query the redis server.  |

### Metrics Collected

|Metric Name               |Description|
|:-------------------------|:----------|
|Redis Connected Clients   |           |
|Redis Key Hits            |           |
