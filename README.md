# 🎨 HandScript Art

**Transform your images with AI-powered handwriting and artistic effects**

[![Demo Video](https://img.shields.io/badge/Demo-Video-red?logo=youtube)](https://www.youtube.com/watch?v=IYbd8CiTPlw)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2.9-green?logo=django)](https://djangoproject.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Latest-orange?logo=tensorflow)](https://tensorflow.org)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- 
## 🎯 Overview

HandScript Art is an innovative AI-powered web application that transforms ordinary images into artistic handwritten-style creations. Using advanced computer vision and deep learning techniques, the application analyzes uploaded images and applies sophisticated artistic filters and transformations to create unique handwritten art pieces.

## ✨ Features

### 🤖 AI-Powered Processing
- **Advanced Computer Vision**: Utilizes OpenCV and TensorFlow for image analysis
- **Deep Learning Models**: Employs pre-trained neural networks for artistic style transfer
- **Intelligent Edge Detection**: Automatic contour and edge analysis for optimal results

### 🎨 Artistic Transformations
- **Handwriting Style Transfer**: Convert images to handwritten art style
- **Multiple Art Filters**: Various artistic effects and transformations
- **Custom Processing**: Tailored algorithms for different image types
- **High-Quality Output**: Maintains image quality during transformation

### 🌐 Modern Web Interface
- **Responsive Design**: Works seamlessly across all devices
- **Drag & Drop Upload**: Intuitive file upload with drag-and-drop support
- **Real-time Processing**: Live progress indicators and status updates
- **Beautiful UI**: Modern glassmorphism design with smooth animations

### 🔧 Technical Features
- **RESTful API**: Clean API endpoints for integration
- **File Validation**: Comprehensive image format and size validation
- **Error Handling**: Robust error management and user feedback
- **Security**: Secure file handling and processing

## 🎬 Demo

Watch our demo video to see HandScript Art in action:

[![Demo Video](https://img.shields.io/badge/🎥_Watch_Demo-YouTube-red?style=for-the-badge)](https://www.youtube.com/watch?v=IYbd8CiTPlw)

## 🛠 Technology Stack

### Backend
- **Framework**: Django 4.2.9
- **API**: Django REST Framework 3.15.2
- **Authentication**: Django Simple JWT 5.3.1
- **Database**: SQLite (development) / PostgreSQL (production)

### AI/ML Libraries
- **Computer Vision**: OpenCV 4.9.0.80
- **Deep Learning**: TensorFlow with GPU support
- **Image Processing**: PIL (Pillow), NumPy 1.24.1
- **Natural Language**: NLTK 3.8.1, TextBlob 0.17.1
- **ML Utils**: scikit-learn, pandas 2.1.4

### Frontend
- **UI**: Modern HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with animations
- **Icons**: Unicode emojis and custom icons
- **Responsive**: Mobile-first design approach

### Additional Tools
- **Data Processing**: pandas, NumPy
- **API Integration**: Google AI Generative Language 0.6.1
- **File Handling**: PyMuPDF 1.23.16, python-multipart
- **Development**: Jupyter Notebook support

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Clone Repository
```bash
git clone https://github.com/yourusername/HandScriptArt.git
cd HandScriptArt
```

### Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file in the root directory:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (optional - uses SQLite by default)
DATABASE_URL=postgresql://user:password@localhost:5432/handscriptart

# AI API Keys (if using external services)
OPENAI_API_KEY=your-openai-key
GOOGLE_AI_API_KEY=your-google-ai-key
```

### Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

### Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

## 📱 Usage

### Basic Usage
1. **Upload Image**: Click "Choose Image" or drag & drop your image
2. **File Validation**: Supported formats: JPG, PNG, GIF (Max: 10MB)
3. **Process**: Click "🚀 Process Image" to start transformation
4. **Download**: Save your artistic creation

### Supported Image Formats
- JPEG/JPG
- PNG
- GIF
- Maximum file size: 10MB

### API Usage
```python
import requests

# Upload and process image
with open('image.jpg', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/api/upload/',
        files={'image': f}
    )
    
result = response.json()
print(f"Processed image URL: {result['processed_url']}")
```

## 📁 Project Structure

```
HandScriptArt/
├── 📁 templates/
│   └── index.html              # Main application interface
├── 📁 static/
│   ├── css/                    # Stylesheets
│   ├── js/                     # JavaScript files
│   └── images/                 # Static images
├── 📁 media/
│   ├── uploads/                # Uploaded images
│   └── processed/              # Processed results
├── 📁 core/
│   ├── models.py               # Database models
│   ├── views.py                # Application views
│   ├── urls.py                 # URL routing
│   └── processors.py           # AI processing logic
├── 📁 api/
│   ├── serializers.py          # API serializers
│   ├── views.py                # API views
│   └── urls.py                 # API routing
├── 📄 requirements.txt         # Python dependencies
├── 📄 manage.py               # Django management script
├── 📄 README.md               # Project documentation
└── 📄 .env.example            # Environment variables template
```

## 🔌 API Endpoints

### Upload & Process
```http
POST /api/upload/
Content-Type: multipart/form-data

Parameters:
- image: File (required) - Image file to process
```

### Get Processing Status
```http
GET /api/status/{task_id}/
```

### Download Processed Image
```http
GET /api/download/{file_id}/
```

### API Response Example
```json
{
  "success": true,
  "task_id": "uuid-task-id",
  "original_filename": "photo.jpg",
  "processed_url": "/media/processed/photo_handscript.jpg",
  "processing_time": 2.34,
  "message": "Image processed successfully"
}
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit Changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to Branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open Pull Request**

### Development Guidelines
- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Ensure cross-platform compatibility

## 🐛 Known Issues & Limitations

- Processing time increases with image size
- Some complex images may require multiple processing attempts
- GPU acceleration recommended for optimal performance

## 🔮 Future Enhancements

- [ ] Multiple artistic style options
- [ ] Batch processing capabilities
- [ ] User accounts and history
- [ ] Mobile application
- [ ] Advanced customization options
- [ ] Social sharing features

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/HandScriptArt/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/HandScriptArt/discussions)

## 🙏 Acknowledgments

- TensorFlow team for deep learning frameworks
- OpenCV community for computer vision tools
- Django developers for the web framework
- All contributors and testers

---

*Transform your memories into art with HandScript Art!*
