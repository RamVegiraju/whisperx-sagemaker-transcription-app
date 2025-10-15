# WhisperX SageMaker Real-Time Inference Deployment
Sample utilizing the LMI v16 container to deploy [WhisperX](https://github.com/m-bain/whisperX/tree/main) on SageMaker Real-Time Endpoints. For whisper3-large you can utilize the vLLM backend as it's a supported architecture: https://docs.vllm.ai/en/v0.7.0/getting_started/examples/whisper.html.

## Additional Hosting Options
- Async Inference: Hybrid inference with built-in queuing, can pass in an S3 path with your input files.
- Payload Restructuring: Pass in an S3 URI as the input payload to your endpoint and have serialization happen within the container, currently happening before endpoint invocation in the sample.