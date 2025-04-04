# DominiSigns: Avatar Translator for Dominican Sign Language

## 📝 Project Description

DominiSigns is an innovative accessibility application that uses artificial intelligence to translate text and voice into Dominican sign language (LSRD) through an animated 3D avatar. Our goal is to break down communication barriers and promote the inclusion of the deaf community in the Dominican Republic.

## 🌟 Key Features

- **Text-to-Sign Translation**: Converts text input into Dominican sign language animations
- **Speech-to-Sign Translation**: Recognizes audio and converts it to signs
- **Customized 3D Avatar**: Realistic avatar that performs signs with precision and fluidity
- **Integrated Dictionary**: Comprehensive LSRD database
- **Accessible Interface**: Designed following universal accessibility principles

## 🚀 Project Status

Currently in active development phase. The project is at the following stages:

- [x] Collection of LSRD dictionary and reference videos
- [ ] Development of text/voice processor
- [ ] Creation of base 3D avatar
- [ ] Implementation of sign animations
- [ ] Development of user interface
- [ ] Testing with the Dominican deaf community

## 🛠️ Technologies Used

- **Frontend**: React, Three.js
- **Backend**: Node.js, Express
- **Language Processing**: TensorFlow/PyTorch for NLP
- **3D Animation**: Blender, Mixamo
- **Generative AI**: Pollinations.ai API
- **Database**: MongoDB

## 📋 Requirements

- Node.js v14 or higher
- Access to Pollinations.ai API
- Dependencies listed in package.json

## 🔧 Installation and Setup

```bash
# Clone the repository
git clone https://github.com/cmunozdev/dominisigns.git
cd dominisigns

# Install dependencies
npm install

# Configure environment variables
cp .env.example .env
# Edit the .env file with your API credentials

# Start the development server
npm run dev
```

## 📊 System Architecture

```
                      ┌───────────────┐
                      │  Text/Audio   │
                      │    Input      │
                      └───────┬───────┘
                              │
                      ┌───────▼───────┐
                      │     NLP       │
                      │   Processor   │
                      └───────┬───────┘
                              │
        ┌───────────┬─────────▼────────┬───────────┐
        │           │                  │           │
┌───────▼───┐ ┌─────▼─────┐    ┌───────▼───┐ ┌─────▼─────┐
│  Syntactic │ │   LSRD    │    │ Animation  │ │   Sign    │
│  Analysis  │ │Translation│    │ Generation │ │ Sequencing│
└───────┬───┘ └─────┬─────┘    └───────┬───┘ └─────┬─────┘
        │           │                  │           │
        └───────────┴─────────┬────────┴───────────┘
                              │
                      ┌───────▼───────┐
                      │      3D       │
                      │    Avatar     │
                      └───────────────┘
```

## 🔍 Use Cases

- **Education**: Support in inclusive classrooms
- **Public Services**: Improved accessibility in hospitals, banks, etc.
- **Personal Communication**: Facilitates everyday interactions
- **Events and Conferences**: Automatic interpretation for presentations

## 🌍 Social Impact

This project is aimed at approximately 100,000 deaf people in the Dominican Republic who use LSRD as their primary means of communication. By providing a technological tool that respects the cultural and linguistic particularities of the country, we seek to:

1. Reduce communication barriers
2. Promote social inclusion
3. Preserve and spread Dominican sign language
4. Support independence and autonomy of the deaf community


## 📜 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

- [National Association of the Deaf of the Dominican Republic](https://ansordo.org)
- Accessibility developer community
- Pollinations.ai team for their technical support
- All interpreters and collaborators who have contributed reference material
