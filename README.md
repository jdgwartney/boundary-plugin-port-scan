# TrueSight Pulse Port Scan Plugin

Measures the time to establish a connection on a TCP/IP port of a network host.

### Prerequisites

|     OS    | Linux | Windows | SmartOS | OS X |
|:----------|:-----:|:-------:|:-------:|:----:|
| Supported |   v   |    v    |    v    |  v   |

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

|Metric Name   |Description                                     |
|:-------------|:-----------------------------------------------|
|PORT\_RESPONSE|Duration of the time to connect to a TCP/IP port|
