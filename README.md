# WhisperX SageMaker Real-Time Inference Deployment
Sample utilizing the LMI v16 container to deploy [WhisperX](https://github.com/m-bain/whisperX/tree/main) on SageMaker Real-Time Endpoints. For whisper3-large you can utilize the vLLM backend as it's a supported architecture: https://docs.vllm.ai/en/v0.7.0/getting_started/examples/whisper.html.

## Additional Hosting Options
- <b>Async Inference</b>: Hybrid inference with built-in queuing, can pass in an S3 path with your input files.
- <b>Payload Restructuring</b>: Pass in an S3 URI as the input payload to your endpoint and have serialization happen within the container, currently happening before endpoint invocation in the sample.

## Docker Debug
Make sure to also test this via Docker on an EC2 instance or a SM Classic NB instance. This simplifies debugging of model script and any serving configurations:
```
#Pull image
docker pull 763104351884.dkr.ecr.us-east-1.amazonaws.com/djl-inference:0.34.0-lmi16.0.0-cu128


#Start container, adjust for path of artifacts
docker run \
  --gpus all \
  -v /home/ubuntu:/opt/ml/model \
  -p 8080:8080 \
  763104351884.dkr.ecr.us-east-1.amazonaws.com/djl-inference:0.34.0-lmi16.0.0-cu128 \
  serve
```