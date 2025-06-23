-- MySQL-compatible seed script for “Students Find Lecturers” app
-- Explicitly targets the `find_my_faculty` database

START TRANSACTION;

-- Step 1: College
INSERT IGNORE INTO find_my_faculty.College (college_id, name) VALUES
    ('CST001', 'College of Science and Technology'),
    ('CMSS001', 'College of Management Social Sciences'),
    ('C0E003', 'College of Engineering'),
    ('CLDS004', 'College of Leadership Development Studies');

-- Step 2: Office
INSERT IGNORE INTO find_my_faculty.Office (office_id, office_number, location, floor, type) VALUES
    ('0123AC', 'A316', 'CST Building', 300, 'STANDARD'),
    ('0124AD', 'A314', 'CST Building', 300, 'STANDARD'),
    ('0125AF', 'A310', 'CST Building', 300, 'STANDARD'),
    ('0126AG', 'A306', 'CST Building', 300, 'STANDARD'),
    ('0127BA', 'CIS Dept. Office A (Right)', 'CST Building', 300, 'CUBICLE'),
    ('0128BB', 'CIS Dept. Office C (Middle)', 'CST Building', 300, 'CUBICLE'),
    ('0129BC', 'CIS Dept. Office B (Right)', 'CST Building', 300, 'CUBICLE'),
    ('0130BD', 'Center of Information and Technology', 'CST Building', 300, 'STANDARD'),
    ('0131BE', 'Center of Info & Tech', 'CST Building', 300, 'STANDARD'),
    ('0132CA', 'Software Eng. Lab, 200 Floor', 'CST Building', 200, 'LABORATORY'),
    ('0133CB', 'A315', 'CST Building', 300, 'STANDARD'),
    ('0134CC', 'A320', 'CST Building', 300, 'STANDARD'),
    ('0135CD', 'D105', 'CMSS', 100, 'STANDARD');

-- Step 3: Department
INSERT IGNORE INTO find_my_faculty.Department (department_id, name, college_id, hod_id, secretary_id) VALUES
    ('012AC', 'C.I.S', 'CST001', NULL, NULL),
    ('013AD', 'Mathematics', 'CST001', NULL, NULL),
    ('014AF', 'Biology', 'CST001', NULL, NULL),
    ('015AG', 'Physics', 'CST001', NULL, NULL),
    ('015GT', 'Estate Management', 'CST001', NULL, NULL),
    ('015AU', 'Architecture', 'CST001', NULL, NULL);

-- Step 4: Lecturer
INSERT IGNORE INTO find_my_faculty.Lecturer (lecturer_id, full_name, office_id, department_id, role, notes) VALUES
    ('00010AI', 'Miss Adeleke Ti-Jesu', '0123AC', '012AC', 'LECTURER', 'CIS, CST Building, 300 Floor'),
    ('00011AJ', 'Miss Ade Nathanael Jemimah', '0123AC', '012AC', 'LECTURER', 'CIS, CST Building, 300 Floor'),
    ('00012AK', 'Mr Henry Ogbu', '0124AD', '012AC', 'LECTURER', 'CIS, CST Building'),
    ('00013AL', 'Prof C.O. Ikoham', '0125AF', '012AC', 'LECTURER', 'CIS, CST Building'),
    ('00014AM', 'Mr Damilola Odunayo', '0126AG', '012AC', 'LECTURER', 'CIS, CST Building'),
    ('00015AN', 'Mr Tope Jegede', '0127BA', '012AC', 'LECTURER', 'Shared space'),
    ('00016BA', 'Mr Ibickpo Dada', '0127BA', '012AC', 'LECTURER', 'Shared space'),
    ('00017BB', 'Mr Ejiboh Chukuebuka', '0128BB', '012AC', 'LECTURER', 'Shared space'),
    ('00018BC', 'Mrs Abiodun Theisah', '0129BC', '012AC', 'LECTURER', 'Shared space'),
    ('00019BD', 'Mr Franklyn Emmanuel', NULL, '012AC', 'LECTURER', 'CIS Dept. Office E (Right), Shared space'),
    ('00020BE', 'Prof Oni Atinuke', '0130BD', '012AC', 'HOD', 'HOD'),
    ('00021CC', 'Mrs Comfort Olamilekan', '0131BE', '012AC', 'SECRETARY', 'Secretary'),
    ('00022CD', 'Mr Otavie Okuyo', '0132CA', '012AC', 'LECTURER', 'Not in 300 Floor'),
    ('00023CE', 'Dr Babalola D.O', '0133CB', '012AC', 'LECTURER', 'CIS, CST Building'),
    ('00024CH', 'Dr Sholauke A.B', '0134CC', '012AC', 'LECTURER', 'CIS, CST Building'),
    ('00025DA', 'Dr Oluranti Jonathan', '0135CD', NULL, 'LECTURER', 'Not in CST building');

-- Step 5: HODLecturer
INSERT IGNORE INTO find_my_faculty.HODLecturer (hod_id, lecturer_id) VALUES
    ('0016FF', '00020BE');

-- Step 6: SecretaryLecturer
INSERT IGNORE INTO find_my_faculty.SecretaryLecturer (secretary_id, lecturer_id) VALUES
    ('0016AF', '00021CC');

-- Step 7: Update Department with HOD & Secretary
UPDATE find_my_faculty.Department
SET hod_id = '0016FF',
    secretary_id = '0016AF'
WHERE department_id = '012AC';

COMMIT;
