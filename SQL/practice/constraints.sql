-- SQL Practice: Constraints
-- Day 3 - Data Engineering Learning Journey

CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,

    patient_name VARCHAR(100) NOT NULL,

    email VARCHAR(150) UNIQUE,

    age INT CHECK (age > 0),

    country VARCHAR(50) DEFAULT 'India'
);

CREATE TABLE VitalSigns (
    vital_id INT PRIMARY KEY,

    patient_id INT NOT NULL,

    heart_rate INT CHECK (heart_rate > 0),

    systolic_bp INT CHECK (systolic_bp > 0),

    diastolic_bp INT CHECK (diastolic_bp > 0),

    FOREIGN KEY (patient_id)
        REFERENCES Patients(patient_id)
);