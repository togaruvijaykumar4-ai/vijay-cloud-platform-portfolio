# Google Colab — Portfolio Setup

Open a new Colab notebook and run:

```python
!git clone https://github.com/togaruvijaykumar4-ai/vijay-cloud-platform-portfolio.git
%cd vijay-cloud-platform-portfolio
!find . -maxdepth 2 -type f | sort | head -100
```

Install Terraform in Colab only when needed:

```bash
!sudo apt-get update -y
!sudo apt-get install -y unzip
!wget -q https://releases.hashicorp.com/terraform/1.13.4/terraform_1.13.4_linux_amd64.zip
!unzip -o terraform_1.13.4_linux_amd64.zip
!sudo mv terraform /usr/local/bin/
!terraform version
```

Do not store cloud access keys in the notebook.
