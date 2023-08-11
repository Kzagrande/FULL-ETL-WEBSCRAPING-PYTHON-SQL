import sys 
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
from datetime import date

extract_scheduling_contract_mock = ExtractContract(
    raw_information_content=[['TO BE PUTAWAY', '', '', 'T3', 'T3', 'T3', 'T3', 'T3', 'T3', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T3'],
                             ['Hours', '', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'],
                             ['% Working Hours', '', '-', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%'], 
                             ['Backlog (To be put away)', '', '-', '7,285', '6,467', '5,767', '7,938', '6,617', '6,311', '6,329', '5,551', '11,097', '13,976', '16,841', '21,237', '23,132', '22,945', '24,366', '31,183', '31,989', '32,795', '32,349', '34,563', '29,847', '39,773', '34,476', '10,056'], 
                             ['Productivity', '', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380', '380'], 
                             ['Direct Labor (CEVA)', '', '', '14', '7', '7', '14', '14', '14', '0', '0', '0', '0', '0', '0', '0', '0', '14', '14', '14', '14', '7', '7', '14', '14', '14', '14'], 
                             ['Planejado'], ['Indirect Labors (CEVA)', '', '', '10', '5', '5', '10', '10', '10', '0', '0', '0', '0', '0', '0', '0', '0', '10', '10', '10', '10', '5', '5', '10', '10', '10', '10'],
                             ['Daily Labors (Productivity)', '', '-', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                             ['Daily Labors (Indirect)', '', '-', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                             ['Total  Labors', '', '-', '24', '12', '12', '24', '24', '24', '0', '24', '24', '24', '24', '12', '12', '24', '48', '24', '24', '24', '12', '12', '24', '24', '24', '24'],
                             ['T4, T5 e T6', '', '-', '20', '20', '20', '', '', '', '', '24', '24', '24', '24', '12', '12', '24', '24', '24', '24', '20', '20', '20', '0', '20', '20', '20'],
                             ['Internal Sinergy'],
                             ['Putaway Throughput per Hour (Planned)', '', '190,926', '7,285', '6,467', '5,767', '5,320', '5,320', '5,320', '', '5,551', '9,120', '9,120', '9,120', '4,560', '4,560', '9,120', '7,220', '14,440', '14,440', '12,920', '10,260', '10,260', '5,320', '12,920', '6,460', '10,056'],
                             ['PutawayThroughput per Hour (Real)', '', '63,211', '4,656', '2,493', '2,841', '1,742', '5,198', '3,773', '1', '1,009', '4,342', '5,588', '4,893', '3,657', '1,875', '625', '8,429', '', '', '', '', '', '', '', '', '12,089'],
                             ['Productivity (Real)', '', '374', '333', '356', '406', '124', '371', '270', '', '', '', '', '', '', '', '', '272', '', '', '', '', '', '', '', '', '864'],
                             ['Mín. Backlog (1h cap.)', '', '', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000'],
                             ['Máx. Backlog (6h cap.)', 'Until Now', 'TOTAL', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000'],
                             ['', '106,558', '193,578', '7,285', '6,467', '5,767', '5,320', '5,320', '5,320', '1', '5,551', '9,120', '9,120', '9,120', '4,560', '4,560', '9,120', '8,355', '14,440', '14,440', '12,920', '10,260', '10,260', '5,320', '12,920', '6,460', '11,572'],
                             ['DAILY MANPOWER OPERATION - OUTBOUND', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '281.1'],
                             [], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Global Productivity'],
                             ['', '', '', '', '', '', '% Realized', '', '', '36.96%', '', '56.81%', '', '55.89%', '', '', '', '', '', '', '', '', 'Backlog IN:', '100,543'],
                             ['', '', '', '', '', '', 'Planned', '', 'Picking:', '191,299', 'Sorting:', '132,761', 'Packing:', '143,569', '', 'Final Backlog:', '24,848', '-0.5%', '% Variation Backlog reduced', '', '', '', 'Backlog OUT:', '24,848'],
                             ['', '', '', '', '', '', 'Real', '', 'Picking:', '70,705', 'Sorting:', '75,415', 'Packing:', '80,245', '', 'Packing Tending:', '160,804'], [], [], [], [], [], [], [], [], [], [], [], [], ['', '', '', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!', '#DIV/0!'],
                             ['TO BE PICKED', 'Until Now', 'TOTAL', 'T3', 'T3', 'T3', 'T3', 'T3', 'T3', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T3'], ['Hours', '', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
                             , ['% Working Hours', '', '-', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%'], ['Consolidated', '', '150,231', '4,656', '2,493', '2,841', '1,742', '5,198', '3,773', '1', '1,009', '4,342', '5,588', '4,893', '3,657', '1,875', '625', '8,429', '14,440', '14,440', '12,920', '10,260', '10,260', '5,320', '12,920', '6,460', '12,089'],
                             ['Backlog (To be picked)', '', '-', '24,981', '23,907', '16,280', '9,929', '9,785', '10,547', '9,595', '5,937', '4,141', '3,243', '4,318', '4,608', '4,292', '2,978', '8,848', '22,527', '26,607', '23,287', '19,827', '21,407', '18,327', '20,887', '13,627', '24,848'],
                             ['Productivity', '', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280', '280'], 
                             ['Direct Labor (CEVA)', '', '', '39', '20', '20', '39', '39', '39', '6', '6', '6', '6', '6', '3', '3', '6', '37', '37', '37', '37', '19', '18', '37', '37', '37', '39'],
                             ['Planejado'], 
                             ['Indirect Labors (CEVA)', '', '', '5', '3', '2', '5', '5', '5', '1', '4', '4', '4', '4', '2', '2', '4', '8', '8', '6', '5', '3', '2', '5', '5', '5', '5'],
                             ['Daily Labors (Productivity)', '', '-', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                             ['Daily Labors (Indirect)', '', '-', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                             ['Total  Labors', '', '-', '44', '23', '22', '44', '44', '44', '7', '10', '10', '10', '10', '5', '5', '10', '45', '45', '43', '42', '22', '20', '42', '42', '42', '44'], ['T4, T5 e T6', '', '-', '12', '12', '12', '', '', '', '', '21', '21', '21', '21', '11', '10', '21', '21', '21', '21', '12', '12', '12', '0', '12', '12', '12'],
                             ['Internal Sinergy'],
                             ['Picking Throughput per Hour (Planned)', '', '191,299', '14,280', '8,960', '8,960', '9,929', '9,785', '10,547', '840', '1,680', '1,680', '1,680', '1,680', '3,920', '3,640', '2,978', '8,120', '10,360', '16,240', '13,720', '8,680', '8,400', '10,360', '13,720', '6,860', '14,280'], ['Picking Throughput per Hour (Real)', '', '70,705', '5158', '3210', '8893', '9123', '4873', '2014', '630', '3790', '5677', '5246', '4243', '2970', '1726', '2451', '761', '', '', '', '', '', '', '', '', '9940'], ['Productivity (Real)', '', '373', '132', '161', '445', '234', '125', '52', '210', '632', '946', '874', '707', '212', '133', '91', '19', '', '', '', '', '', '', '', '', '255'], ['Mín. Backlog (1h picking cap.)', '', '', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000'], ['Máx. Backlog (6h picking cap.)', 'Until Now', 'TOTAL', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000', '30,000'], ['', '114,089', '202,429', '14,280', '8,960', '8,960', '9,929', '9,785', '10,547', '840', '3,686', '5,177', '5,141', '3,846', '3,920', '3,640', '2,978', '8,120', '10,360', '16,240', '13,720', '8,680', '8,400', '10,360', '13,720', '6,860', '14,280'], ['TO BE SORTED', '', '', 'T3', 'T3', 'T3', 'T3', 'T3', 'T3', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T3'], ['Hours', '', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], ['% Working Hours', '', '-', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%'], ['Picking Throughput per Hour', '', '', '5,158', '3,210', '8,893', '9,123', '4,873', '2,014', '630', '3,790', '5,677', '5,246', '4,243', '2,970', '1,726', '2,451', '761', '10,360', '16,240', '13,720', '8,680', '8,400', '10,360', '13,720', '6,860', '9,940'], ['Backlog (To be Sorted)', '', '-', '5,062', '2,579', '5,432', '6,884', '1,418', '1,640', '1,375', '2,346', '3,508', '4,126', '3,670', '3,114', '2,779', '1,570', '401', '8,729', '16,240', '13,720', '10,095', '11,540', '14,945', '17,965', '12,520', '7,088'], ['Productivity', '', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535', '535'], ['Direct Labor (CEVA)', '', '', '21', '11', '10', '21', '21', '21', '3', '3', '3', '3', '3', '2', '1', '3', '20', '20', '20', '20', '10', '10', '20', '20', '20', '21'], ['Planejado'], ['Indirect Labors (CEVA)', '', '', '6', '3', '3', '6', '6', '6', '3', '6', '6', '6', '6', '3', '3', '6', '8', '8', '8', '5', '3', '2', '5', '5', '5', '6'], ['Daily Labors (Productivity)', '', '-', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['Daily Labors (Indirect)', '', '-', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['Total  Labors', '', '-', '27', '14', '13', '27', '27', '27', '6', '9', '9', '9', '9', '5', '4', '9', '28', '28', '28', '25', '13', '12', '25', '25', '25', '27'], ['T4, T5 e T6', '', '-', '3', '3', '3', '', '', '', '', '15', '15', '15', '15', '8', '7', '15', '15', '15', '15', '3', '3', '3', '0', '3', '3', '3'], ['Internal Sinergy'], ['Sorting Throughput per Hour (Planned)', '', '132,761', '5,062', '2,579', '5,432', '6,884', '1,418', '1,640', '803', '2,346', '3,508', '4,126', '3,670', '3,114', '2,779', '1,570', '401', '8,729', '16,240', '12,305', '6,955', '6,955', '10,700', '12,305', '6,153', '7,088'], ['Sorting Throughput per Hour (Real)', '', '75,415', '6,442', '6,024', '5,688', '7,395', '9,879', '1,973', '795', '2,795', '4,169', '4,650', '4,576', '3,495', '2,129', '3,454', '2,032', '', '', '', '', '', '', '', '', '9,919'], ['Productivity (Real)', '', '366', '307', '548', '569', '352', '470', '94', '530', '155', '232', '258', '254', '350', '266', '192', '81', '', '', '', '', '', '', '', '', '472'], ['Mín. Backlog (1h Sorting cap.)', '', '', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000', '3,000'], ['Máx. Backlog (3h Sorting cap.)', 'Until Now', 'TOTAL', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000', '18,000'], ['', '72,720', '153,062', '6,426', '5,656', '5,217', '7,066', '9,547', '1,968', '803', '2,599', '3,803', '4,628', '4,485', '3,190', '2,779', '3,355', '1,906', '8,729', '16,240', '12,305', '6,955', '6,955', '10,700', '12,305', '6,153', '9,294'], ['TO BE PACKED', '', '', 'T3', 'T3', 'T3', 'T3', 'T3', 'T3', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T3'], ['Hours', '', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], ['% Working Hours', '', '-', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%'], ['Sorting Throughput per Hour', '', '155,757', '6,442', '6,024', '5,688', '7,395', '9,879', '1,973', '795', '2,795', '4,169', '4,650', '4,576', '3,495', '2,129', '3,454', '2,032', '8,729', '16,240', '12,305', '6,955', '6,955', '10,700', '12,305', '6,153', '9,919'], ['Backlog (To be Packed)', '', '-', '10,570', '5,241', '4,435', '4,367', '5,941', '618', '1,333', '3,252', '3,579', '3,823', '2,412', '2,059', '2,100', '3,443', '2,971', '8,946', '16,240', '12,305', '6,955', '6,955', '10,700', '12,305', '6,153', '7,391'], ['Productivity', '', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202', '202'], ['Direct Labor (CEVA)', '', '', '57', '39', '38', '57', '57', '57', '8', '8', '8', '8', '8', '4', '4', '8', '55', '55', '55', '55', '28', '27', '55', '55', '55', '57'], ['Planejado'], ['Indirect Labors (CEVA)', '', '', '7', '4', '3', '7', '7', '7', '1', '5', '5', '5', '5', '3', '2', '5', '11', '11', '8', '7', '3', '3', '7', '7', '7', '7'], ['Daily Labors (Productivity)', '', '-', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['Daily Labors (Indirect)', '', '-', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['Total  Labors', '', '-', '64', '43', '41', '64', '64', '64', '9', '13', '13', '13', '13', '7', '6', '13', '66', '66', '63', '62', '31', '30', '62', '62', '62', '64'], ['T4, T5 e T6', '', '-', '8', '8', '8', '', '', '', '', '30', '30', '30', '30', '15', '15', '30', '30', '30', '30', '8', '8', '8', '0', '8', '8', '8'], ['Internal Sinergy'], ['Packing Throughput per Hour (Planned)', '', '143,569', '10,570', '5,241', '4,435', '4,367', '5,941', '618', '808', '3,252', '3,579', '3,823', '2,412', '2,059', '2,100', '3,443', '2,971', '8,946', '16,240', '12,305', '6,955', '6,955', '10,700', '12,305', '6,153', '7,391'], ['Packing Throughput per Hour (Real)', '', '80,245', '5,115', '12,131', '6,116', '7,813', '8,786', '7,389', '203', '1,012', '4,019', '4,374', '6,176', '4,043', '2,014', '2,397', '2,754', '', '', '', '', '', '', '', '', '5,903'], ['Productivity (Real)', '', '150', '90', '311', '161', '137', '154', '130', '51', '27', '106', '115', '163', '213', '106', '300', '100', '', '', '', '', '', '', '', '', '91'], ['Mín. Backlog (1h packed cap.)', '', '', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000'], ['Máx. Backlog (4h packed cap.)', 'Until Now', 'TOTAL', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000'], ['', '88,008', '168,567', '10,570', '11,285', '5,873', '7,702', '8,472', '6,653', '808', '3,252', '3,751', '3,947', '5,767', '4,023', '2,100', '3,443', '2,971', '8,946', '16,240', '12,305', '6,955', '6,955', '10,700', '12,305', '6,153', '7,391'], ['TO BE BOXED', '', '', 'T3', 'T3', 'T3', 'T3', 'T3', 'T3', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T1', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T2', 'T3'], ['Hours', '', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], ['% Working Hours', '', '-', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '50%', '100%'], ['Packing Throughput per Hour', '', '160,804', '5,115', '12,131', '6,116', '7,813', '8,786', '7,389', '203', '1,012', '4,019', '4,374', '6,176', '4,043', '2,014', '2,397', '2,754', '8,946', '16,240', '12,305', '6,955', '6,955', '10,700', '12,305', '6,153', '5,903'], ['Backlog (To be Boxed)', '', '-', '4,346', '12,131', '12,247', '15,260', '13,246', '9,835', '203', '1,012', '4,019', '4,374', '6,176', '4,043', '2,014', '2,397', '2,754', '8,946', '16,240', '12,305', '8,460', '13,015', '21,315', '22,820', '18,173', '18,676'], ['Productivity', '', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200', '1200'], ['Direct Labor (CEVA)', '', '', '9', '5', '4', '9', '9', '9', '2', '2', '2', '2', '2', '1', '1', '2', '9', '9', '9', '9', '2', '2', '9', '9', '9', '9'], ['Indirect Labors (CEVA)', '', '', '2', '1', '1', '2', '2', '2', '1', '2', '2', '2', '2', '1', '1', '2', '3', '3', '3', '2', '1', '1', '2', '2', '2', '2'], ['Daily Labors (Productivity)', '', '-', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['Daily Labors (Indirect)', '', '-', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['Total  Labors', '', '-', '11', '6', '5', '11', '11', '11', '3', '4', '4', '4', '4', '2', '2', '4', '12', '12', '12', '11', '3', '3', '11', '11', '11', '11'], ['T4, T5 e T6', '', '-', '', '', '', '', '', '', '', '5', '5', '5', '5', '3', '2', '5', '5', '5', '5', '0', '0', '0', '0', '0', '0', '0'], ['Internal Sinergy'], ['Boxed Throughput per Hour (Planned)', '', '152,159', '4,346', '6,000', '4,800', '10,800', '10,800', '9,835', '203', '1,012', '4,019', '4,374', '6,176', '4,043', '2,014', '2,397', '2,754', '8,946', '16,240', '10,800', '2,400', '2,400', '10,800', '10,800', '5,400', '10,800'], ['Boxed Throughput per Hour (Real)'], ['Productivity (Real)'], ['Mín. Backlog (1h packed cap.)', '', '', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000', '5,000'], ['Máx. Backlog (4h packed cap.)', 'Until Now', 'TOTAL', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000', '20,000'], ['', '', '152,159', '4,346', '6,000', '4,800', '10,800', '10,800', '9,835', '203', '1,012', '4,019', '4,374', '6,176', '4,043', '2,014', '2,397', '2,754', '8,946', '16,240', '10,800', '2,400', '2,400', '10,800', '10,800', '5,400', '10,800']],
        extraction_date=date.today()
)   