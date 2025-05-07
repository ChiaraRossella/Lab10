from database.DB_connect import DBConnect
from modello.country import Country


class DAO():
    @staticmethod
    def getAllConnectedCountries(anno: int, idMap: dict[Country]):
        archi=[]
        conn=DBConnect.get_connection()
        cursor=conn.cursor(dictionary=True)
        query= """select distinct c.state1no, c.state2no 
                    from contiguity as c 
                    where c.conttype = 1 and state1no < state2no and year<= %s """

        cursor.execute(query, (anno,))
        for r in cursor:
            archi.append((idMap[r.state1no], idMap[r.state2no]))

        cursor.close()
        conn.close()
        return archi

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from country")
        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result
