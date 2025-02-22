CREATE DATABASE inventory_prototype_X;
USE inventory_prototype_X;


-- Drop existing table if needed
--DROP TABLE IF EXISTS awb_details;

-- Create new AWB table with updated column types
CREATE TABLE awb_details (
    AWB varchar(50) PRIMARY KEY,
    MAWB varchar(50) DEFAULT 0,
    AWB_date DATE,
    freight_fordwarder VARCHAR(50),
    Amount DECIMAL(10,2) NOT NULL,
    Currency VARCHAR(10),       -- Allows multi-character currency codes (e.g., USD, INR)
    Supplier VARCHAR(50),
    Goods_types VARCHAR(50),
    Clearance VARCHAR(50),
    Number_of_boxes INT,
    weight FLOAT,
    unit_of_measure VARCHAR(20), -- Allows full names like "Kilograms", "Meters"
    volumetric_weight FLOAT
);


select * from awb_details;



