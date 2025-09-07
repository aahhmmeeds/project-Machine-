# 🚀 دليل رفع مشاريع الماشين ليرنينج على GitHub

## 📋 المتطلبات الأساسية

### 1. إنشاء حساب GitHub
- اذهب إلى [GitHub.com](https://github.com)
- أنشئ حساب جديد إذا لم يكن لديك حساب

### 2. تثبيت Git
- حمل Git من [git-scm.com](https://git-scm.com)
- ثبته على جهازك

## 🎯 المشاريع الجاهزة للرفع

لديك **5 مشاريع** جاهزة للرفع:

1. **🏦 Churn_Modelling** - توقع ترك العملاء للبنك
2. **👥 Emp_attrition** - توقع ترك الموظفين للعمل
3. **🌧️ Weather_AUS_Machine_learning** - توقع الطقس الأسترالي
4. **🎗️ breast-cancer** - تصنيف سرطان الثدي
5. **🧠 alzheimer-s-disease** - تحليل مرض الزهايمر

## 📝 خطوات الرفع لكل مشروع

### الخطوة 1: إنشاء Repository على GitHub

1. اذهب إلى [GitHub.com](https://github.com)
2. اضغط على **"New repository"** (الزر الأخضر)
3. املأ البيانات:
   - **Repository name**: اختر اسم مناسب (انظر الأسماء المقترحة أدناه)
   - **Description**: وصف المشروع
   - ✅ **Public** (عام)
   - ❌ لا تختر "Add a README file"
   - ❌ لا تختر ".gitignore"
   - ❌ لا تختر "license"
4. اضغط **"Create repository"**

### الخطوة 2: أوامر Git لكل مشروع

#### 🏦 مشروع Churn_Modelling
```bash
cd "d:\ML Project\Churn_Modelling"
git init
git add .
git commit -m "Initial commit: Customer Churn Prediction ML Project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/customer-churn-prediction.git
git push -u origin main
```

#### 👥 مشروع Emp_attrition
```bash
cd "d:\ML Project\Emp_attrition"
git init
git add .
git commit -m "Initial commit: HR Employee Attrition Prediction App"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/hr-employee-attrition-app.git
git push -u origin main
```

#### 🌧️ مشروع Weather_AUS_Machine_learning
```bash
cd "d:\ML Project\Weather_AUS_Machine_learning"
git init
git add .
git commit -m "Initial commit: Australian Weather Prediction App"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/australian-weather-prediction.git
git push -u origin main
```

#### 🎗️ مشروع breast-cancer
```bash
cd "d:\ML Project\breast-cancer"
git init
git add .
git commit -m "Initial commit: Breast Cancer Classification ML Project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/breast-cancer-classification.git
git push -u origin main
```

#### 🧠 مشروع alzheimer-s-disease
```bash
cd "d:\ML Project\alzheimer-s-disease"
git init
git add .
git commit -m "Initial commit: Alzheimer's Disease Analysis ML Project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/alzheimers-disease-analysis.git
git push -u origin main
```

## 📛 أسماء Repository المقترحة

| المشروع | الاسم المقترح |
|---------|---------------|
| Churn_Modelling | `customer-churn-prediction` |
| Emp_attrition | `hr-employee-attrition-app` |
| Weather_AUS_Machine_learning | `australian-weather-prediction` |
| breast-cancer | `breast-cancer-classification` |
| alzheimer-s-disease | `alzheimers-disease-analysis` |

## ⚠️ ملاحظات مهمة

1. **استبدل `YOUR_USERNAME`** باسم المستخدم الخاص بك على GitHub
2. **تأكد من وجود الملفات** قبل تشغيل الأوامر:
   - `README.md`
   - `requirements.txt`
   - ملفات المشروع الأساسية
3. **إذا واجهت خطأ في المصادقة**:
   - استخدم Personal Access Token بدلاً من كلمة المرور
   - اذهب إلى GitHub Settings > Developer settings > Personal access tokens

## 🔧 إعداد Git (مرة واحدة فقط)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 📊 ما تم إنجازه

✅ **README.md** لكل مشروع  
✅ **requirements.txt** لكل مشروع  
✅ **.gitignore** للمجلد الرئيسي  
✅ **توثيق شامل** لكل مشروع  

## 🎉 بعد الرفع

بعد رفع المشاريع بنجاح:
1. **شارك روابط المشاريع** مع الآخرين
2. **أضف Topics** لكل repository (machine-learning, python, data-science)
3. **اكتب وصف جيد** لكل مشروع
4. **أضف صور** أو screenshots إذا أمكن

## 🆘 المساعدة

إذا واجهت أي مشاكل:
1. تأكد من تثبيت Git بشكل صحيح
2. تأكد من إنشاء Repository على GitHub أولاً
3. تأكد من استبدال `YOUR_USERNAME` باسمك الحقيقي
4. استخدم Command Prompt أو PowerShell كمسؤول

---
🌟 **بالتوفيق في رفع مشاريعك!**
