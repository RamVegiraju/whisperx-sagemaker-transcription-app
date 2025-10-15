import os
import json
import time
import boto3
import whisperx
import torch

# ---- prepare audio ----
audio_path = "test_audio.mp4"
audio = whisperx.load_audio(audio_path)
sample_rate = 16000

payload = {
    "audio_array": audio.tolist(),
    "sample_rate": sample_rate
}

# prepare runtime client to invoke EP
endpoint_name = "Enter endpoint name here"
runtime = boto3.client("sagemaker-runtime", region_name="us-east-1")

# ---- overall timing ----
start_total = time.time()

for i in range(100):
    start_iter = time.time()

    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Accept="application/json",
        Body=json.dumps(payload)
    )

    result = json.loads(response["Body"].read())
    duration = time.time() - start_iter
    print(f"[{i+1}/100] Inference took {duration:.2f} seconds")

# ---- total elapsed ----
total_time = time.time() - start_total
print(f"\n✅ Completed 100 invocations in {total_time:.2f} seconds "
      f"(avg {total_time/100:.2f} s per call)")
