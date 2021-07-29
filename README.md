# playgrounds-timestream-nvidia
 

This is just a simple script to pull metrics from a prometheus exporter exposing Nvidia GPU metrics and push the data into AWS TimeStream database

Can be easily wrapped in a lambda, but at the moment it is running locally and hitting virtual hosts running [Nvidia Prometheus Exporter](https://github.com/mindprince/nvidia_gpu_prometheus_exporter)


# other metrics

Since this works with any prometheus /metrics endpoint, you can simply deploy any [existing exporter](https://prometheus.io/docs/instrumenting/exporters/) and connect it here. 

## what's the point? why not just use a prometheus server

high level data flow:
prometheus exporter >> lambda pulls /metric, pushes to >> AWS TimeStream  >> Grafana/QuickSight/etc.

One obvious benefit is an entirely serverless data backend, AWS TimeStream removes the headache of scaling backend resources (scaling prometheus server is not fun and openTSDB is obsolete)