# Mobile Programming
# Index
[History](#android-history) [Contents](#contents) [Exam Guide](#exam-guide) [Features](#features) [Architecture](#android-architecture)
----------

## Date 23/12
## Linux Kernel
- Security, Memory management, Process Management
- Acts as abstraction Layer between Hardware and rest of software stack.

## Libraries

- runs in Sys background
- Uses C/C+ Lang
  ### 4 types of Libraries
    - Core lib
      - System C lib 
      - Media Lib : MPEG4,H.264,MP3,AAC, JPG,programming
      - Surface Manager
        - 2D 3D layers
      - Webkit
        - Web browser in Mobile
      - SGL
        - 2D graphics engine
      - 3D Lib
        - OpenGL ES 1.0 
      - Free type
        - Bitmap vector font rendering
      - SQLite Lib
  ## Android Runtime
      - Dalvik Virtual Machine
        - Register based
        - Executable files in Dalvik
        - Multiple VM can run at same time
        - 1 DVM instance for 1 Applications
        - Dx tool in SDK can transform compiled java class into .dex format
      - DVM vs JVM
        - DVM
          - Google, Dalvik executable
        - JVM
          - By oracle
          
        
![Activity LifeCycle](https://i2.wp.com/androhub.com/wp-content/uploads/2015/04/activity_lifecycle.png?)


----------
## Date 16/12

### Exam Guide
#### 100 Marks
    - Internal (40 Marks)
        - Class test (10 Marks) (Feb Mid)
        - Viva - Project(20 Marks)
        - Assignment (10 Marks)
    - External (60 Marks)
        - Mention XML, Not GUI
        - Paper has time constraint
        - Paper is maximum programming based subject



## Contents
- Android - History, Frameworks
- UI Controls - Text field, Tab activity, Label, Layouts, toast, Event Handling, Image view, List view
- Intent - Multi Screen / Window Activity - Menu
- Database - Internal (SQLite), External (PHP)
----------


## Android History
- OHA (Open Handset Alliance) Aims:
    - Accelerate innovation
    - Richer exp, Less expensive
- OHA develops Android, the first complete, open and free mobile platform
- Google bought OHA


## What is Android?
- Android is a software stack for mobile which includes OS, Middleware and Key Applications.
- Provides APIs, SDKs to build using Android Platform(JAVA(Dalvik) /Kotlin), Node js(C#)  

## Features
- Reuse and replacement of components
- JVM Dalvik
- Graphics Processing (2D/3D) using OpenGL ES 1.0
- Open Source Web Browser - Web kit
- SQLite
- Multimedia
- Rich Dev env (emulators, debugging, memory probe, logging ~~eclipse plugins~~) 
- Hardware Dependent:
    - GSM Telephony
    - Bluetooth, EDGE, 3G, 4G, 5G and Wi-Fi Support
    - Camera, GPS, Compass, Accelerometer & more sensors

## Android Architecture

![Architecture](https://elinux.org/images/c/c2/Android-system-architecture.jpg)



