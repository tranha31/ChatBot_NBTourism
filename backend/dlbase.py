import rdfextras
from rdflib import query
rdfextras.registerplugins()

import rdflib

g = rdflib.Graph()
filename = "../data/owl_dulich_nb_v2.owl"

g.parse(filename, format='xml')

class DLBase:
    def __init__(self) -> None:
        pass

    ###lay thong tin danh lam
    def getInfoPlace(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?name ?nameEx ?location ?info
        WHERE
        {
        ?x ex:tenDanhLam ?name;
        ex:coViTriTai ?y;
        ex:coDacDiem ?z.

        ?y ex:tenDiaDiem ?location. 
        ?z ex:noiDungDacDiem ?info.
        OPTIONAL{?x ex:tenDanhLamKhac ?nameEx}
        FILTER(lcase(?name) = \""""+value+"""\" || lcase(?nameEx) = \""""+value+"""\")    
        } LIMIT 1"""
        
        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['name'] = str(row.name)
            d['nameEx'] = str(row.nameEx)
            d['location'] = str(row.location)
            d['info'] = str(row.info)
            result.append(d)
        
        return result

    ###lay thong tin le hoi
    def getFesitvalInfo(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?name ?nameEx ?location ?time ?purpose ?cultral ?activities
        WHERE
        {
        ?x ex:tenLeHoi ?name;
        ex:toChucTai ?y;
        ex:toChucVao ?z;
        ex:coMucDich ?m;
        ex:hoatDongVH ?c.

        ?y ex:tenDiaDiem ?location. 
        ?z ex:thoiGianToChuc ?time.
        ?m ex:noiDungMucDich ?purpose.
        ?c ex:noiDungHoatDong ?cultral.
        OPTIONAL
        {
            ?x ex:tenKhac ?nameEx.  
        }
        FILTER(lcase(?name) = \""""+value+"""\" || lcase(?nameEx) = \""""+value+"""\")
        }
        LIMIT 1"""

        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['name'] = str(row.name)
            d['nameEx'] = str(row.nameEx)
            d['location'] = str(row.location)
            d['time'] = str(row.time)
            d['purpose'] = str(row.purpose)
            d['cultral'] = str(row.cultral)
            d['activities'] = str(row.activities)
            result.append(d)
        
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?activities
        WHERE
        {
        ?x ex:tenLeHoi ?name;
            ex:hoatDongVC ?c.
        ?c ex:noiDungHoatDong ?activities.

        FILTER(lcase(?name) = \""""+value+"""\")
        }
        LIMIT 1
        """
        rows = g.query(query)
        for row in rows:
            result[0]['activities'] = str(row.activities)
            break

        return result

    ###vi tri danh lam
    def getLocationPlace(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?location
        WHERE
        {
        ?x ex:tenDanhLam ?name;
            ex:coViTriTai ?y.

        ?y ex:tenDiaDiem ?location. 
        OPTIONAL{?x ex:tenDanhLamKhac ?nameEx}
        FILTER(lcase(?name) = \""""+value+"""\" || lcase(?nameEx) = \""""+value+"""\") 
        }LIMIT 1"""

        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['location'] = str(row.location)
            result.append(d)
        
        return result

    ###dia diem to chuc le hoi
    def getLocationFestival(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?location
        WHERE
        {
        ?x ex:tenLeHoi ?name;
        ex:toChucTai ?y.

        ?y ex:tenDiaDiem ?location. 
        OPTIONAL
        {
            ?x ex:tenKhac ?nameEx.    
        }
        FILTER(lcase(?name) = \""""+value+"""\" || lcase(?nameEx) = \""""+value+"""\")
        }
        LIMIT 1"""

        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['location'] = str(row.location)
            result.append(d)
        
        return result
    
    ###hoat dong le hoi
    def getActivitiesFestival(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?cultral ?activities
        WHERE
        {
        ?x ex:tenLeHoi ?name;
        ex:hoatDongVH ?c.

        ?c ex:noiDungHoatDong ?cultral.
        FILTER(lcase(?name) = \""""+value+"""\") 
        }
        LIMIT 1"""

        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['cultral'] = str(row.cultral)
            d['activities'] = str(row.activities)
            result.append(d)
        
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?activities
        WHERE
        {
        ?x ex:tenLeHoi ?name;
            ex:hoatDongVC ?c.
        ?c ex:noiDungHoatDong ?activities.

        FILTER(lcase(?name) = \""""+value+"""\")
        }
        LIMIT 1
        """
        rows = g.query(query)
        for row in rows:
            result[0]['activities'] = str(row.activities)

        return result

    ###muc dich le hoi
    def getPurposeFestival(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?purpose
        WHERE
        {
        ?x ex:tenLeHoi ?name;
            ex:coMucDich ?m.
        ?m ex:noiDungMucDich ?purpose.

        FILTER(lcase(?name) = \""""+value+"""\")
        }
        LIMIT 1
        """
        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['purpose'] = str(row.purpose)
            result.append(d)
        return result
    
    ###thoi gian to chuc le hoi
    def getTimeHoldFestival(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?time
        WHERE
        {
        ?x ex:tenLeHoi ?name;
            ex:toChucVao ?z.
        ?z ex:thoiGianToChuc ?time.
        FILTER(lcase(?name) = \""""+value+"""\")
        }
        LIMIT 1
        """
        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['time'] = str(row.time)
            result.append(d)
        return result

    ###thong tin tour
    def getInfoTour(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?name ?description ?condition ?costPackage1 ?infoPackage1 ?costPackage2 ?infoPackage2 ?planDay ?planAfter
        WHERE
        {
        ?x ex:tenTour ?name;
        ex:moTaTour ?description;
        ex:coDieuKien ?c;
        ex:coLichTrinh ?l;
        ex:coChiPhi ?m1;
        ex:coChiPhi2 ?m2.

        ?c ex:noiDungDieuKien ?condition.
        ?m1 ex:chiPhiGoi ?costPackage1;
        ex:thongTinGoi ?infoPackage1.
        ?m2 ex:chiPhiGoi ?costPackage2;
        ex:thongTinGoi ?infoPackage2.
        ?l ex:lichTrinhBuoiSang ?planDay.
        OPTIONAL
        {
            ?l ex:lichTrinhBuoiChieu ?planAfter.
        }
        FILTER(lcase(?name) = \""""+value+"""\")
        }
        LIMIT 1
        """
        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['name'] = str(row.name)
            d['description'] = str(row.description)
            d['condition'] = str(row.condition)
            d['costPackage1'] = str(row.costPackage1)
            d['infoPackage1'] = str(row.infoPackage1)
            d['costPackage2'] = str(row.costPackage2)
            d['infoPackage2'] = str(row.infoPackage2)
            d['planDay'] = str(row.planDay)
            d['planAfter'] = str(row.planAfter)
            result.append(d)
        return result
    
    ###chi phi tour
    def getCostTour(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?costPackage1 ?infoPackage1 ?costPackage2 ?infoPackage2
        WHERE
        {
        ?x ex:tenTour ?name;
        ex:coChiPhi ?m1;
        ex:coChiPhi2 ?m2.

        ?m1 ex:chiPhiGoi ?costPackage1;
        ex:thongTinGoi ?infoPackage1.
        ?m2 ex:chiPhiGoi ?costPackage2;
        ex:thongTinGoi ?infoPackage2.
        FILTER(lcase(?name) = \""""+value+"""\")
        }
        LIMIT 1
        """
        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['costPackage1'] = str(row.costPackage1)
            d['infoPackage1'] = str(row.infoPackage1)
            d['costPackage2'] = str(row.costPackage2)
            d['infoPackage2'] = str(row.infoPackage2)
            result.append(d)
        return result

    ###lich trinh tour
    def getPlanTour(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?planDay ?planAfter
        WHERE
        {
        ?x ex:tenTour ?name;
           ex:coLichTrinh ?l.
        ?l ex:lichTrinhBuoiSang ?planDay.
        OPTIONAL
        {
            ?l ex:lichTrinhBuoiChieu ?planAfter.
        }
        FILTER(lcase(?name) = \""""+value+"""\")
        }
        LIMIT 1
        """

        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['planDay'] = str(row.planDay)
            d['planAfter'] = str(row.planAfter)
            result.append(d)
        return result

    ###goi y le hoi
    def getSuggestFestival(self, status, value):
        value = str(value)
        result = []
        rows = []
        if status == 0:
            query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
            SELECT DISTINCT ?name ?nameEx
            WHERE
            {
            ?x ex:tenLeHoi ?name.
            ?x ex:toChucVaoThang ?m.

            ?m ex:thangBatDau ?t1;
            ex:thangKetThuc ?t2.
            OPTIONAL
            {
                ?x ex:tenKhac ?nameEx.    
            }
            FILTER(?t1 <= xsd:integer(\""""+value+"""\") && ?t2 >= xsd:integer(\""""+value+"""\"))
            }
            """
            rows = g.query(query)

        else:
            query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
            SELECT DISTINCT ?name ?nameEx
            WHERE
            {
            ?x ex:tenLeHoi ?name.
            ?x ex:coMucDich ?m.

            ?m ex:noiDungMucDich ?t1.
            OPTIONAL
            {
                ?x ex:tenKhac ?nameEx.    
            }
            FILTER(regex(lcase(?t1),\""""+value+"""\"))
            }
            """
            rows = g.query(query)
        
        for row in rows:
            d = {}
            d['name'] = str(row.name)
            d['nameEx'] = str(row.nameEx)
            result.append(d)
        return result

    ###goi y tour
    def getSuggestTour(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?name
        WHERE
        {
        ?x ex:tenTour ?name.
        FILTER(regex(lcase(?name),\""""+value+"""\"))
        }
        """
        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['name'] = str(row.name)
            result.append(d)
        return result

    ###Lay thong tin nha hang
    def getInfoRestaurant(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?name ?vitri
        WHERE
        {
        ?x ex:tenDanhLam ?n;
            ex:coViTriTai ?m.
        ?m ex:thuocHuyen ?huyen.
        ?y ex:tenNhaHang ?name;
            ex:viTriNhaHang ?vitri;
            ex:thuocHuyen ?huyen.
        FILTER(regex(lcase(?n),\""""+value+"""\"))
        }
        """
        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['name'] = str(row.name)
            d['vitri'] = str(row.vitri)
            result.append(d)
        return result

    ###Lay thong tin khach san
    def getInfoHotel(self, value):
        query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xml: <http://www.w3.org/XML/1998/namespace>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ex: <http://www.semanticweb.org/taha/ontologies/2021/10/untitled-ontology-3#>
        SELECT DISTINCT ?name ?vitri ?gia ?link
        WHERE
        {
        ?x ex:tenDanhLam ?n;
            ex:coViTriTai ?m.
        ?m ex:thuocHuyen ?huyen.
        ?y ex:tenKhachSan ?name;
            ex:viTriKhachSan ?vitri;
            ex:giaKhachSan ?gia;
            ex:linkKhachSan ?link;
            ex:thuocHuyen ?huyen.
        FILTER(regex(lcase(?n),\""""+value+"""\"))
        }
        """
        rows = g.query(query)
        result = []
        for row in rows:
            d = {}
            d['name'] = str(row.name)
            d['vitri'] = str(row.vitri)
            d['gia'] = str(row.gia)
            d['link'] = str(row.link)
            result.append(d)
        return result