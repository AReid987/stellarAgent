Skip to main content
Search PyPI
Search
Help Sponsors Log in Register
portkey-ai 1.10.1

pip install portkey-ai
Copy PIP instructions

Latest version

Released: Jan 9, 2025

Python client library for the Portkey API

Navigation
 Project description
 Release history
 Download files
Verified details 
These details have been verified by PyPI
Maintainers
 ayush-portkey
Unverified details
These details have not been verified by PyPI
Project links
Homepage
Meta
License: MIT License
Author: Portkey.ai
Requires: Python >=3.8
Provides-Extra: dev, langchain-callback, llama-index-callback
Classifiers
License
OSI Approved :: MIT License
Operating System
OS Independent
Programming Language
Python :: 3
Project description


Control Panel for AI Apps
pip install portkey-ai

Features

The Portkey SDK is built on top of the OpenAI SDK, allowing you to seamlessly integrate Portkey's advanced features while retaining full compatibility with OpenAI methods. With Portkey, you can enhance your interactions with OpenAI or any other OpenAI-like provider by leveraging robust monitoring, reliability, prompt management, and more features - without modifying much of your existing code.

AI Gateway
Unified API Signature
If you've used OpenAI, you already know how to use Portkey with any other provider.	Interoperability
Write once, run with any provider. Switch between any model from_any provider seamlessly.
Automated Fallbacks & Retries
Ensure your application remains functional even if a primary service fails.	Load Balancing
Efficiently distribute incoming requests among multiple models.
Semantic Caching
Reduce costs and latency by intelligently caching results.	Virtual Keys
Secure your LLM API keys by storing them in Portkey vault and using disposable virtual keys.
Request Timeouts
Manage unpredictable LLM latencies effectively by setting custom request timeouts on requests.
Observability
Logging
Keep track of all requests for monitoring and debugging.	Requests Tracing
Understand the journey of each request for optimization.
Custom Metadata
Segment and categorize requests for better insights.	Feedbacks
Collect and analyse weighted feedback on requests from users.
Analytics
Track your app & LLM's performance with 40+ production-critical metrics in a single place.
Usage
Prerequisites
Sign up on Portkey and grab your Portkey API Key
Add your OpenAI key to Portkey's Virtual Keys page and keep it handy
# Installing the SDK

$ pip install portkey-ai
$ export PORTKEY_API_KEY=PORTKEY_API_KEY

Making a Request to OpenAI
Portkey fully adheres to the OpenAI SDK signature. You can instantly switch to Portkey and start using our production features right out of the box.

Just replace from openai import OpenAI with from portkey_ai import Portkey:
from portkey_ai import Portkey

portkey = Portkey(
    api_key="PORTKEY_API_KEY",
    virtual_key="VIRTUAL_KEY"
)

chat_completion = portkey.chat.completions.create(
    messages = [{ "role": 'user', "content": 'Say this is a test' }],
    model = 'gpt-4'
)

print(chat_completion)

Async Usage
Use AsyncPortkey instead of Portkey with await:
import asyncio
from portkey_ai import AsyncPortkey

portkey = AsyncPortkey(
    api_key="PORTKEY_API_KEY",
    virtual_key="VIRTUAL_KEY"
)

async def main():
    chat_completion = await portkey.chat.completions.create(
        messages=[{'role': 'user', 'content': 'Say this is a test'}],
        model='gpt-4'
    )

    print(chat_completion)

asyncio.run(main())

Compatibility with OpenAI SDK

Portkey currently supports all the OpenAI methods, including the legacy ones.

Methods	OpenAI
V1.26.0	Portkey
V1.3.1
Audio	✅	✅
Chat	✅	✅
Embeddings	✅	✅
Images	✅	✅
Fine-tuning	✅	✅
Batch	✅	✅
Files	✅	✅
Models	✅	✅
Moderations	✅	✅
Assistants	✅	✅
Threads	✅	✅
Thread - Messages	✅	✅
Thread - Runs	✅	✅
Thread - Run - Steps	✅	✅
Vector Store	✅	✅
Vector Store - Files	✅	✅
Vector Store - Files Batches	✅	✅
Generations	❌ (Deprecated)	✅
Completions	❌ (Deprecated)	✅
Portkey-Specific Methods
Methods	Portkey
V1.3.1
Feedback	✅
Prompts	✅
Check out Portkey docs for the full list of supported providers

 

Contributing

Get started by checking out Github issues. Email us at support@portkey.ai or just ping on Discord to chat.

Project details
Verified details 
These details have been verified by PyPI
Maintainers
 ayush-portkey
Unverified details
These details have not been verified by PyPI
Project links
Homepage
Meta
License: MIT License
Author: Portkey.ai
Requires: Python >=3.8
Provides-Extra: dev, langchain-callback, llama-index-callback
Classifiers
License
OSI Approved :: MIT License
Operating System
OS Independent
Programming Language
Python :: 3


Release history
Release notifications | RSS feed 
THIS VERSION
	
	

1.10.1

Jan 9, 2025

	
	

1.10.0

Jan 3, 2025

	
	

1.9.10

Dec 26, 2024

	
	

1.9.9

Dec 11, 2024

	
	

1.9.8

Dec 5, 2024

	
	

1.9.7

Nov 29, 2024

	
	

1.9.6

Nov 26, 2024

	
	

1.9.5

Nov 21, 2024

	
	

1.9.4

Nov 7, 2024

	
	

1.9.3

Oct 22, 2024

	
	

1.9.2

Oct 18, 2024

	
	

1.9.1

Oct 9, 2024

	
	

1.9.0

Oct 8, 2024

	
	

1.8.7

Sep 4, 2024

	
	

1.8.6

Aug 31, 2024

	
	

1.8.5

Aug 28, 2024

	
	

1.8.4

Aug 26, 2024

	
	

1.8.3

Aug 23, 2024

	
	

1.8.2

Aug 16, 2024

	
	

1.8.1

Aug 13, 2024

	
	

1.8.0

Aug 12, 2024

	
	

1.7.2

Jul 31, 2024

	
	

1.7.1

Jul 25, 2024

	
	

1.7.1rc1 PRE-RELEASE

Jul 25, 2024

	
	

1.7.0

Jul 3, 2024

	
	

1.7.0rc1 PRE-RELEASE

Jul 3, 2024

	
	

1.6.0 YANKED

Jun 28, 2024

	
	

1.5.1

Jun 26, 2024

	
	

1.5.0

Jun 22, 2024

	
	

1.4.1

Jun 18, 2024

	
	

1.4.0

Jun 6, 2024

	
	

1.3.2

Jun 1, 2024

	
	

1.3.1

May 31, 2024

	
	

1.3.0

May 31, 2024

	
	

1.2.4

Apr 13, 2024

	
	

1.2.3

Apr 5, 2024

	
	

1.2.2

Mar 23, 2024

	
	

1.2.1

Mar 22, 2024

	
	

1.2.0

Mar 21, 2024

	
	

1.1.7

Feb 13, 2024

	
	

1.1.6

Feb 2, 2024

	
	

1.1.5

Jan 24, 2024

	
	

1.1.4

Jan 17, 2024

	
	

1.1.3

Jan 12, 2024

	
	

1.1.2

Jan 9, 2024

	
	

1.1.1

Jan 8, 2024

	
	

1.1.0

Jan 2, 2024

	
	

1.0.1

Jan 2, 2024

	
	

1.0.0

Dec 8, 2023

	
	

0.1.53

Oct 10, 2023

	
	

0.1.52

Sep 21, 2023

	
	

0.1.51

Sep 20, 2023

	
	

0.1.50

Sep 19, 2023

	
	

0.1.49

Sep 16, 2023

	
	

0.1.48

Sep 14, 2023

	
	

0.1.47

Sep 13, 2023

	
	

0.1.46

Sep 13, 2023

	
	

0.1.45

Sep 12, 2023

	
	

0.1.44

Sep 11, 2023

	
	

0.1.43

Sep 11, 2023

	
	

0.1.42

Sep 11, 2023

	
	

0.1.41

Sep 11, 2023

	
	

0.1.40

Sep 11, 2023

	
	

0.1.39

Sep 9, 2023

	
	

0.1.38

Sep 9, 2023

	
	

0.1.37

Sep 9, 2023

	
	

0.1.36

Sep 9, 2023

	
	

0.1.35

Sep 9, 2023

	
	

0.1.34

Sep 9, 2023

	
	

0.1.32

Sep 9, 2023

	
	

0.1.31

Sep 7, 2023

	
	

0.1.30

Sep 7, 2023

	
	

0.1.29

Sep 7, 2023

	
	

0.1.28

Sep 6, 2023

	
	

0.1.27

Sep 5, 2023

Download files

Download the file for your platform. If you're not sure which to choose, learn more about installing packages.

Source Distribution
	
portkey_ai-1.10.1.tar.gz (305.4 kB view details)

Uploaded Jan 9, 2025 Source

Built Distribution
	
portkey_ai-1.10.1-py3-none-any.whl (578.7 kB view details)

Uploaded Jan 9, 2025 Python 3

File details

Details for the file portkey_ai-1.10.1.tar.gz.

File metadata
Download URL: portkey_ai-1.10.1.tar.gz
Upload date: Jan 9, 2025
Size: 305.4 kB
Tags: Source
Uploaded using Trusted Publishing? No
Uploaded via: twine/6.0.1 CPython/3.9.21
File hashes
Hashes for portkey_ai-1.10.1.tar.gz
Algorithm	Hash digest	
SHA256	c393df3ee0996d3d4217442019d40e0ca7806beacec5da6f66bd13bd9efc47f1	Copy
MD5	dc0965eb7a3d80f335adc3c96942812c	Copy
BLAKE2b-256	3c72e3d78a91ad5d6f657055f19f2bb6acda18b88087df8de337d8bd3159824f	Copy

See more details on using hashes here.

File details

Details for the file portkey_ai-1.10.1-py3-none-any.whl.

File metadata
Download URL: portkey_ai-1.10.1-py3-none-any.whl
Upload date: Jan 9, 2025
Size: 578.7 kB
Tags: Python 3
Uploaded using Trusted Publishing? No
Uploaded via: twine/6.0.1 CPython/3.9.21
File hashes
Hashes for portkey_ai-1.10.1-py3-none-any.whl
Algorithm	Hash digest	
SHA256	f177da3553ea347b490d4b7c747fb7578eeb9d278708dd2e8b1b86c035b6ffdb	Copy
MD5	b6506170c8b6ed2353b8557e6d5cef94	Copy
BLAKE2b-256	b77e483675f899153b6cc9dc61f3ccc3cd582ced39a6f21a0269bd3efd40cb09	Copy

See more details on using hashes here.

Help
Installing packages
Uploading packages
User guide
Project name retention
FAQs
About PyPI
PyPI Blog
Infrastructure dashboard
Statistics
Logos & trademarks
Our sponsors
Contributing to PyPI
Bugs and feedback
Contribute on GitHub
Translate PyPI
Sponsor PyPI
Development credits
Using PyPI
Code of conduct
Report security issue
Privacy Notice
Terms of Use
Acceptable Use Policy

Status: all systems operational

Developed and maintained by the Python community, for the Python community.
Donate today!

"PyPI", "Python Package Index", and the blocks logos are registered trademarks of the Python Software Foundation.


© 2025 Python Software Foundation
Site map

 English español français 日本語 português (Brasil) українська Ελληνικά Deutsch 中文 (简体) 中文 (繁體) русский עברית Esperanto 한국어
AWS
Cloud computing and Security Sponsor
Datadog
Monitoring
Fastly
CDN
Google
Download Analytics
Pingdom
Monitoring
Sentry
Error logging
StatusPage
Status page