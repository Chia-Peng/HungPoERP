import pandas as pd


hexRod = {
    "外徑(mm)": ['6', '8', '9', '9.5', '10', '11', '12', '14', '17', '19', '21', '22', '23', '24', '25', '26', '27', '29', '30', '32', '35', '36', '38', '41', '45', '46'],
    "每米重量(kg)": ['0.25', '0.44', '0.56', '0.62', '0.69', '0.83', '0.99', '1.34', '1.98', '2.45', '3.03', '3.32', '3.63', '3.95', '4.29', '4.64', '5.00', '5.77', '6.17', '7.02', '8.40', '8.89', '9.91', '11.53', '13.89', '14.52']
}


class pandasDataframe():
    def __init__(self):
        pass

    def Create(file_name):
        df = pd.DataFrame(hexRod)
        print("使用字典來建立df：")
        print(df)

        # saving the excelsheet
        df.to_excel(file_name)
        print('Sales record successfully exported into Excel File')

    def Delete():
        pass

    def Read(file_name):
        df = pd.read_excel(file_name)
        return df

    def Update():
        pass

    def arrayFormat(array):
        strArray = []
        for i in array:
            strArray.append(str(i))
        return strArray
