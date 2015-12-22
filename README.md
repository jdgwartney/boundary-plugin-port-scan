# TrueSight Pulse Port Scan Plugin

Measures the time to establish a connection on a TCP/IP port of a host.

### Prerequisites

|     OS    | Linux | Windows | SmartOS | OS X |
|:----------|:-----:|:-------:|:-------:|:----:|
| Supported |   v   |    v    |    v    |  v   |

#### For TrueSight Pulse Meter v4.2 or later

- To install new meter go to Settings->Installation or [see instructions](https://help.boundary.com/hc/en-us/sections/200634331-Installation).

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

|Metric Name   |Description                                                  |
|:-------------|:------------------------------------------------------------|
|PORT\_RESPONSE|Duration of the time to connect to a TCP/IP port             |
|PORT\_STATUS  |Indicates if the port is open or closed: 0 - Closed, 1 - Open|
