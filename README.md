# playgrounds-timestream-nvidia
 

This is just a simple script to pull metrics from a prometheus exporter exposing Nvidia GPU metrics and push the data into AWS TimeStream database

Can be easily wrapped in a lambda, but at the moment it is running locally and hitting virtual hosts running [Nvidia Prometheus Exporter](https://github.com/mindprince/nvidia_gpu_prometheus_exporter)