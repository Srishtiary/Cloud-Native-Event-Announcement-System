# Cloud-Native-Event-Announcement-System
Cloud-native event notification web app using AWS services: S3, Lambda, API Gateway, and SNS.

## 📖 Project Overview
This project is a **Cloud-Native Event Announcement System** built using AWS services.  
It allows an organizer to publish an event through a web interface, and all subscribed users automatically receive the announcement via email.

---

## 🏗️ Architecture
- **Frontend**: HTML, CSS, JavaScript hosted on **Amazon S3** (Static Website Hosting).  
- **API Layer**: **Amazon API Gateway (HTTP API)** connects the frontend with the backend.  
- **Backend**: **AWS Lambda (Python)** processes event submissions.  
- **Notifications**: **Amazon SNS** sends announcement emails to all subscribers.  

---

## ⚙️ Tech Stack
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (AWS Lambda)  
- **AWS Services**:  
  - Amazon S3 (Static Website Hosting)  
  - Amazon API Gateway (HTTP API)  
  - AWS Lambda  
  - Amazon SNS (Email Notifications)  

---

## ✨ Features
- 📩 **Subscribe via Email** → Users can subscribe to receive event notifications.  
- 📢 **Publish Event** → Organizer submits an event from the web form.  
- 🔔 **Auto Email Notification** → All subscribers instantly get notified via email.  

---

## 🚀 How It Works
1. User opens the hosted frontend (S3 Static Website).  
2. User fills out the **Event Form** (event title & details).  
3. Form data is sent via **API Gateway (HTTP API)** to **Lambda**.  
4. Lambda publishes the event to **SNS Topic**.  
5. All **SNS Subscribers** receive an email notification with the event details.  

---

## 📊 Architecture Diagram
User → S3 → API Gateway (HTTP API) → Lambda → SNS 

---

## 🔮 Future Enhancements
- Add authentication for event publishing.  
- Store past events in a database (DynamoDB).  
- Create an admin dashboard to view/manage events.  
