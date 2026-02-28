# 🔐 Python Multithreaded Port Scanner

A fast and lightweight **TCP Port Scanner** built using Python for learning and practicing fundamental cybersecurity and networking concepts.

This project was developed as part of my cybersecurity engineering learning journey to understand how network reconnaissance tools work internally.

---

## 🚀 Features

* ✅ TCP Connect Port Scanning
* ✅ Multithreaded Scanning (Fast Performance)
* ✅ Domain → IP Resolution
* ✅ Common Service Detection
* ✅ Scan Time Measurement
* ✅ Automatic Result Logging
* ✅ Error Handling & Stable Execution

---

## 🧠 Concepts Learned

This project demonstrates practical understanding of:

* Socket Programming
* TCP Networking
* Port Enumeration
* Multithreading
* Network Reconnaissance Techniques
* Python Automation

---

## ⚙️ Technologies Used

* **Python 3**
* `socket` module
* `threading` module
* `time` module

---

## 📂 Project Structure

```
python-port-scanner/
│
├── scanner.py
├── results.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone Repository

```
git clone https://github.com/your-username/python-port-scanner.git
```

### 2. Navigate to Project

```
cd python-port-scanner
```

### 3. Run Scanner

```
python scanner.py
```

---

## 🧪 Example Usage

```
Enter target: scanme.nmap.org
Start port: 20
End port: 100
```

### Example Output

```
[OPEN] Port 22 | Service: SSH
[OPEN] Port 80 | Service: HTTP

Scan Completed!
Total Open Ports: 2
Time Taken: 3.12 seconds
Results saved to results.txt
```

---

## 📄 Output

All discovered open ports are automatically saved inside:

```
results.txt
```

---

## ⚠️ Legal Disclaimer

This tool is created **strictly for educational purposes**.

Only scan:

* Your own systems
* Authorized lab environments
* Practice platforms

Unauthorized network scanning may be illegal.

---

## 🎯 Learning Objective

The goal of this project is to understand the working principles behind professional network scanning tools such as Nmap and similar reconnaissance utilities.

---

## 👨‍💻 Author

**Rajendra Redkar**
Cybersecurity Engineering Student

---

## ⭐ Future Improvements

* Banner Grabbing
* CLI Argument Support
* Colored Terminal Interface
* OS Detection
* UDP Scanning

---

## 📜 License

This project is open-source and available under the MIT License.


