import streamlit as st

#########################################################################################################################

# # Fonction pour le projet 1 - Toys & Models
def projet_1():
    page_selection_projet_1 = st.sidebar.radio("Choisir une section : ", ["Consignes", "SQL", "Images", "Conclusion"], key="projet_1")
#------------------------------------------------------------------------------------------------------------------------
    if page_selection_projet_1 == "Consignes":
        st.title("SQL & Power BI : Consignes")

        st.subheader("Introduction :")
        st.markdown("""
        <div style="text-align: justify;">
            Vous êtes mandaté par l'entreprise Toys & Models qui vend des modèles et des maquettes.<br>
            L’entreprise possède déjà une base de données qui répertorie les employés, les produits, les commandes et bien plus encore. 
            Vous êtes invité à explorer et découvrir cette base de données.<br>
            <b>Le directeur de l’entreprise souhaite avoir un tableau de bord qu’il pourrait actualiser chaque matin pour obtenir les dernières informations afin de gérer l’entreprise.</b>
        </div><br>
        """, unsafe_allow_html=True)

        st.subheader("Objectif & Enjeux :")
        st.markdown("""
                <div style="text-align: justify;">
                Votre tableau de bord doit s’articuler autour de ces 4 sujets principaux : ventes, finances, logistique, et ressources humaines.
                <br><br>
                BLA BLA BLA
                </div><br>
                """, unsafe_allow_html=True)

        st.subheader("Ressources :")
        st.markdown("""
            <div style="text-align: justify;">
            </div><br>
            """, unsafe_allow_html=True)

        # Créer une section rétractable (expander) pour afficher l'image cliquable
        with st.expander("Afficher/Cacher le schéma de la base de données"):
            st.markdown("""
                <a href="https://i72.servimg.com/u/f72/20/11/38/84/diagra10.png" target="_blank">
                    <img src="https://i72.servimg.com/u/f72/20/11/38/84/diagra10.png" alt="Schéma de la base de données" style="width: 100%; height: auto;">
                </a>
                """, unsafe_allow_html=True)
                   
        st.subheader("Outils :")
        st.markdown("""
        <div style="text-align: justify;">
        Le directeur ne souhaite pas travailler avec SQL mais veut accéder aux données automatiquement et graphiquement.
        Vous pouvez proposer l’outil de votre choix (Power BI, Tableau, etc.), tant que le tableau de bord est pertinent.<br>
        Base de données SQL : Vous avez le choix entre vous connecter au serveur cloud ou déployer le script localement. Les données sont identiques dans les deux cas.
        </div><br>
        """, unsafe_allow_html=True)

        st.subheader("Livrable attendu :")
        st.markdown("""
        <div style="text-align: justify;">
        Vous donnerez une courte présentation de votre tableau de bord (demandez à votre formateur la durée).<br>
        La présentation doit inclure : Vue d’ensemble du contexte, présentation de l’équipe et des outils utilisés.<br>
        Démonstration de votre tableau de bord, et interprétation des KPI métiers.<br>
        Difficultés rencontrées et perspectives d’évolution.<br>
        N’hésitez pas à créer des KPI supplémentaires !
        </div><br>
        """, unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------
    elif page_selection_projet_1 == "Images":
        st.title("SQL & Power BI : Images")
        st.write("Voici les copies d'écran issues de la représentation faite sur Power BI :")
        
          # Liste des images pour la navigation avec flèches
        images = [
            "https://i72.servimg.com/u/f72/20/11/38/84/a-rh110.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/a-rh210.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/b-vent10.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/b-vent11.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/b-vent13.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/b-vent12.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/b-vent14.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/c-fina11.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/c-fina10.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/c-fina12.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/c-fina14.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/c-fina13.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/c-fina15.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/d-logi10.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/d-logi11.png",
            "https://i72.servimg.com/u/f72/20/11/38/84/d-logi12.png"
        ]
   
        for image_url in images:
            st.image(image_url, use_container_width=True)
#------------------------------------------------------------------------------------------------------------------------
    elif page_selection_projet_1 == "SQL":
        st.title("SQL & Power BI : Requêtes SQL")
        
        st.write("""
            Voici un exemple de code SQL utilisé pour la partie Logistique :
            """)

        # Ajouter un expander pour un autre exemple
        with st.expander("Afficher/Cacher le code SQL"):
            sql_logistique = """
            SELECT 
                customers.country AS `Pays_client`,
                productLine AS `Catégorie_produit`,
                products.productName AS `Nom_produit`,
                productScale AS `Echelle`,
                DATE_FORMAT(orders.orderDate, "%d/%m/%Y") AS `Date_commande`,
                DATE_FORMAT( orders.shippedDate, "%d/%m/%Y") AS `Date_envoi`,
                DATEDIFF(orders.shippedDate, orders.orderDate) AS `Délai_envoi`
            FROM products
            JOIN orderdetails ON products.productCode = orderdetails.productCode
            JOIN orders ON orderdetails.orderNumber = orders.orderNumber
            JOIN customers ON customers.customerNumber = orders.customerNumber
            WHERE orders.status = "Shipped"
            ;
            """
            st.code(sql_logistique, language="sql")

        st.write("""
            Voici un exemple de code SQL utilisé pour la partie Finances :
            """)
        # Ajouter un autre expander pour un autre code SQL
        with st.expander("Afficher/Cacher le code SQL"):
            sql_finances = """
            SELECT 
                `Année`,
                    CASE
                    WHEN `Mois` = 1 THEN "01"
                    WHEN `Mois` = 2 THEN "02"
                    WHEN `Mois` = 3 THEN "03"
                    WHEN `Mois` = 4 THEN "04"
                    WHEN `Mois` = 5 THEN "05"
                    WHEN `Mois` = 6 THEN "06"
                    WHEN `Mois` = 7 THEN "07"
                    WHEN `Mois` = 8 THEN "08"
                    WHEN `Mois` = 9 THEN "09"
                    WHEN `Mois` = 10 THEN "10"
                    WHEN `Mois` = 11 THEN "11"
                    WHEN `Mois` = 12 THEN "12"
                END as `Mois`,
                CASE
                    WHEN `Mois` = 1 THEN "01-Janvier"
                    WHEN `Mois` = 2 THEN "02-Février"
                    WHEN `Mois` = 3 THEN "03-Mars"
                    WHEN `Mois` = 4 THEN "04-Avril"
                    WHEN `Mois` = 5 THEN "05-Mai"
                    WHEN `Mois` = 6 THEN "06-Juin"
                    WHEN `Mois` = 7 THEN "07-Juillet"
                    WHEN `Mois` = 8 THEN "08-Aout"
                    WHEN `Mois` = 9 THEN "09-Septembre"
                    WHEN `Mois` = 10 THEN "10-Octobre"
                    WHEN `Mois` = 11 THEN "11-Novembre"
                    WHEN `Mois` = 12 THEN "12-Décembre"
                END as `Libellé_Mois`,
                    `Pays_Client`,
                    `Nom_client`,
                    `Catégorie`,
                    SUM(`Total_ventes`) AS `CA`
            FROM
            (
                SELECT
                        orders.orderNumber AS `Numéro_commande`,
                        YEAR(orders.orderDate) AS `Année`,
                        MONTH(orders.orderDate) AS `Mois`,
                        customers.country AS `Pays_client`,
                        customers.customerName AS `Nom_client`,
                        products.productLine AS `Catégorie`,
                        SUM((orderdetails.quantityOrdered * orderdetails.priceEach)) AS `Total_ventes`
                    FROM products
                    JOIN orderdetails ON products.productCode = orderdetails.productCode
                    JOIN orders ON orderdetails.orderNumber = orders.orderNumber
                    JOIN customers ON customers.customerNumber = orders.customerNumber
                    WHERE orders.status != "Cancelled"
                    GROUP BY `Numéro_commande`, `Catégorie`
            ) AS `R1`
            GROUP BY `Pays_Client`, `Nom_client`, `Catégorie`, `Année`, `Mois`
            ORDER BY `Année` DESC, `Mois` DESC, `Pays_client`ASC
            ;          
            """
            st.code(sql_finances, language="sql")
        
        st.write("""
            Voici un exemple de code SQL utilisé pour la partie Ressources Humaines :
            """)

        # Ajouter un expander pour afficher le code SQL
        with st.expander("Afficher/Cacher le code SQL"):
            sql_rh = """           
            WITH `Ventes` AS 
            (
                SELECT 
                    `Num_client`,
                    `Num_vendeur`,
                    SUM(`CA_facture`) AS `CA_client`,
                    SUM(`Nb_commande`) AS `Nb_commandes_client`
                FROM
                (
                    SELECT 
                        orderdetails.orderNumber AS `Num_commande`,
                        customers.customerNumber AS `Num_client`,
                        customers.salesRepEmployeeNumber AS `Num_vendeur`,
                        COUNT(orders.orderNumber) AS `Nb_commande`,
                        SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS `CA_facture`
                    FROM orderdetails
                    JOIN orders ON orders.orderNumber = orderdetails.orderNumber
                    JOIN customers ON customers.customerNumber = orders.customerNumber
                    WHERE orders.status != "Cancelled"
                    GROUP BY `Num_commande`, `Num_client`, `Num_vendeur`
                ) AS `R1`
                GROUP BY `Num_client`, `Num_vendeur`
            ),
            `Vendeurs` AS
            (
                SELECT 
                    offices.country AS `Pays_bureau`,
                    offices.city AS `Ville_bureau`,
                    employees.employeeNumber AS `Num_vendeur`,
                    employees.firstName AS `Nom_vendeur`,
                    employees.lastName AS `Prénom_vendeur`
                FROM employees
                JOIN offices ON offices.officeCode = employees.officeCode
                WHERE employees.jobTitle = "Sales Rep"
            )
            SELECT 
                `Pays_bureau`,
                `Ville_bureau`,
                CONCAT(`Nom_vendeur`, " ", `Prénom_vendeur`) AS `Employé`,
                COUNT(`Num_client`) AS `Nb_client`,
                SUM(`CA_client`) AS `CA_vendeur`,
                SUM(`CA_client`) / COUNT(`Num_client`) AS `CA_par_client`,
                SUM(`Nb_commandes_client`) AS `Nb_commandes`,
                SUM(`CA_client`) / SUM(`Nb_commandes_client`) AS `CA_par_commande`   
                
            FROM `Vendeurs`
            LEFT JOIN `Ventes` ON Ventes.Num_vendeur = Vendeurs.Num_vendeur
            GROUP BY `Pays_bureau`, `Ville_bureau`, `Employé`
            ;
            """
            st.code(sql_rh, language="sql")

        st.write("""Voici un exemple de code SQL utilisé pour la partie Ventes :""")
        
        # Ajouter un expander pour afficher/cacher le code SQL
        with st.expander("Afficher/Cacher le code SQL Ventes"):
            sql_ventes = """
            SELECT 
                `Bureau`,
                `Catégorie_produit`,
                `Année`,
                CASE
                    WHEN `Mois` = 1 THEN "01"
                    WHEN `Mois` = 2 THEN "02"
                    WHEN `Mois` = 3 THEN "03"
                    WHEN `Mois` = 4 THEN "04"
                    WHEN `Mois` = 5 THEN "05"
                    WHEN `Mois` = 6 THEN "06"
                    WHEN `Mois` = 7 THEN "07"
                    WHEN `Mois` = 8 THEN "08"
                    WHEN `Mois` = 9 THEN "09"
                    WHEN `Mois` = 10 THEN "10"
                    WHEN `Mois` = 11 THEN "11"
                    WHEN `Mois` = 12 THEN "12"
                END as `Mois`,
                CASE
                    WHEN `Mois` = 1 THEN "01-Janvier"
                    WHEN `Mois` = 2 THEN "02-Février"
                    WHEN `Mois` = 3 THEN "03-Mars"
                    WHEN `Mois` = 4 THEN "04-Avril"
                    WHEN `Mois` = 5 THEN "05-Mai"
                    WHEN `Mois` = 6 THEN "06-Juin"
                    WHEN `Mois` = 7 THEN "07-Juillet"
                    WHEN `Mois` = 8 THEN "08-Aout"
                    WHEN `Mois` = 9 THEN "09-Septembre"
                    WHEN `Mois` = 10 THEN "10-Octobre"
                    WHEN `Mois` = 11 THEN "11-Novembre"
                    WHEN `Mois` = 12 THEN "12-Décembre"
                END as `Libellé_Mois`,
                `Qté_commandée_année_N`,
                `Qté_commandée_année_N-1`,
                ROUND((`Qté_commandée_année_N`-`Qté_commandée_année_N-1`) / `Qté_commandée_année_N-1`, 4)  AS `Variation`
            FROM (
                SELECT 
                    offices.country AS `Bureau`,
                    productlines.productLine AS `Catégorie_produit`,
                    YEAR(orders.orderdate) AS `Année`,    
                    MONTH(orders.orderdate) AS `Mois`,
                    LAG(SUM(orderdetails.quantityOrdered))
                        OVER (PARTITION BY productlines.productLine, MONTH(orders.orderdate)
                        ORDER BY productlines.productLine, MONTH(orders.orderdate), YEAR(orders.orderdate))
                    AS `Qté_commandée_année_N-1`,
                    SUM(orderdetails.quantityOrdered) AS `Qté_commandée_année_N`
                FROM productlines
                JOIN products ON productlines.productline = products.productline
                JOIN orderdetails ON products.productCode = orderdetails.productCode
                JOIN orders ON orders.orderNumber = orderdetails.orderNumber
                JOIN customers ON customers.customerNumber = orders.customerNumber
                JOIN employees ON employees.employeeNumber = customers.salesRepEmployeeNumber
                JOIN offices ON offices.officeCode = employees.officeCode
                WHERE orders.status != "Cancelled"
                GROUP BY
                    `Bureau`,
                    `Catégorie_produit`,
                    `Année`,
                    `Mois`
            ) AS `R1`
            ORDER BY `Année` DESC, `Mois` DESC, `Bureau` ASC;
            """
            st.code(sql_ventes, language="sql")

#------------------------------------------------------------------------------------------------------------------------
    elif page_selection_projet_1 == "Conclusion":
        st.title("SQL & Power BI : Conclusion")
        st.markdown("""
        <div style="text-align: justify;">
        Lors de mon analyse des différentes dimensions de la base de données, j’ai pu identifier des points forts ainsi que des axes d’amélioration pour chacun des domaines.
        Ces observations révèlent des opportunités concrètes pour améliorer nos performances globales et renforcer notre organisation.
        </div><br>
        """, unsafe_allow_html=True)

        st.subheader("1. Domaine RH :")
        st.markdown("""
            <div style="text-align: justify;">
                J’ai constaté une inégalité dans la répartition des clients et du chiffre d’affaires par vendeur. Certains vendeurs n’ont aucun client rattaché (et n’ont donc pas déclenché 1 seule vente), ce qui rend difficile l’évaluation équitable de leurs performances.
            </div>
                <u>Recommandations :</u>
            <div style="text-align: justify;">
                Nous devrions enrichir la base de données avec des informations supplémentaires, telles que les temps de travail, les dates d’entrée et de sortie. À terme, cela nous permettra de mieux comparer les performances des vendeurs et de détecter les éventuelles inefficacités.
            </div>
            <br>
        """, unsafe_allow_html=True)

        st.subheader("2. Domaine Ventes :")
        st.markdown("""
            <div style="text-align: justify;">
                Mon analyse a montré qu’un client sur cinq n’est pas rattaché à un vendeur, ce qui limite le suivi et l’accompagnement des clients. En Allemagne particulièrement, un nombre significatif de clients semble non attribué, ce qui peut refléter un déséquilibre dans la répartition des vendeurs au niveau international.
                J’ai également identifié un produit en stock qui n’a généré aucune vente, mettant en évidence une opportunité commerciale non exploitée.
            </div>
                <u>Recommandations :</u>
            <div style="text-align: justify;">
                Nous devons mettre en place un rattachement systématique de chaque client à un vendeur dès son enregistrement. Cela renforcera le suivi client et optimisera la relation commerciale. En parallèle, il serait pertinent de revoir la répartition de nos équipes commerciales, notamment pour couvrir des territoires géographiques et stratégiques comme l’Allemagne.
                Enfin, il serait utile de signaler aux équipes commerciales les produits ayant des difficultés de vente pour envisager des promotions ou des offres groupées adaptées.
            </div>
            <br>
        """, unsafe_allow_html=True)

        st.subheader("3. Domaine Finances :")
        st.markdown("""
            <div style="text-align: justify;">
                J’ai observé une croissance encourageante de 33 % du chiffre d’affaires entre 2022 et 2023.
                Cependant, certains crédits accordés à nos clients semblent excessifs par rapport à leur chiffre d’affaires cumulé, ce qui constitue un risque financier.
                En parallèle, j’ai relevé des écarts dans les paiements, notamment des impayés ou des trop-perçus, qui impactent directement notre trésorerie.
            </div>
                <u>Recommandations :</u>
            <div style="text-align: justify;">
                Nous devons ajuster les crédits accordés pour qu’ils soient alignés avec le chiffre d’affaires réel de chaque client.
                Il est essentiel de surveiller les écarts de paiements et d’intégrer des contrôles rigoureux pour éviter les erreurs, comme des paiements sur des commandes annulées.
                Dans ce cas, il est crucial d’informer le client concerné pour régulariser la situation rapidement en déclenchant une nouvelle vente par exemple.
            </div>
            <br>
        """, unsafe_allow_html=True)

        st.subheader("4. Domaine Logistique : ")
        st.markdown("""
            <div style="text-align: justify;">
                J’ai constaté que le stock moyen par produit est actuellement de 15 mois, un niveau bien supérieur à nos besoins.
                De plus, certaines commandes restent non expédiées, ce qui pourrait refléter des erreurs dans notre système de gestion des statuts de commande.
            </div>
                <u>Recommandations :</u>
            <div style="text-align: justify;">
                J’ai constaté que le stock moyen par produit est actuellement de 15 mois, un niveau bien supérieur à nos besoins.
                De plus, certaines commandes restent non expédiées, ce qui pourrait refléter des erreurs dans notre système de gestion des statuts de commande.
            </div>
            <br>
        """, unsafe_allow_html=True)

        st.subheader("Conclusion générale : ")
        st.markdown("""
            <div style="text-align: justify;">
                Nos résultats, et notamment la forte croissance du chiffre d’affaires en 2023, sont très encourageants.
                Cependant, des efforts sont nécessaires pour structurer davantage nos processus internes et limiter les risques liés à la finance, à la logistique et aux ventes.
            </div>
                <u>Recommandations :</u>
            <div style="text-align: justify;">
                Nous devons consolider notre croissance en optimisant nos processus.
                Cela implique une meilleure gestion des ressources humaines, une relation client renforcée, un suivi rigoureux de la trésorerie, et une gestion plus efficace des stocks.
                En adoptant ces mesures, nous serons en mesure de renforcer la santé financière de l’entreprise et de maintenir une dynamique de croissance pérenne.
            </div>
            <br>
        """, unsafe_allow_html=True)

#########################################################################################################################

# Fonction pour la page d'accueil
def accueil():
    st.title("Portfolio de Ludovic Simunek :")

    # Résumé
    st.write("Fort de plus de 20 ans d’expérience en ressources humaines et en gestion des données, je souhaite aujourd’hui valoriser mes compétences en analyse de données en tant que Data Analyst.")
    st.write("Spécialiste d’Excel, VBA et Access, je maîtrise l’automatisation et l’organisation des données pour éclairer les prises de décision stratégiques. Mon parcours m’a permis de concevoir des outils d’analyse efficaces, d’optimiser les workflows informatiques et de produire des reportings précis répondant aux besoins stratégiques.")
    st.write("Doté d’un esprit rigoureux et orienté solutions, je suis déterminé à accompagner les organisations dans l’exploitation de leurs données pour améliorer leur performance et leur stratégie globale.")
    st.write("N'hésitez pas à naviguer sur mes différents projets.")
    st.write("")
    st.write("Ludovic Simunek")
    
#########################################################################################################################

# Fonction pour le projet 2
def projet_2():
    st.title("Projet 2 : Analyse de Films")
    st.write("BLA BLA BLA")

#########################################################################################################################

# Fonction pour le projet 3
def projet_3():
    st.title("Projet 3 : ")
    st.write("BLA BLA BLA")

#########################################################################################################################

# Fonction pour le projet 4
def projet_4():
    st.title("Projet 4 : ")
    st.write("BLA BLA BLA")

#########################################################################################################################

# Fonction pour le projet 5
def projet_5():
    st.title("Projet 5 : ")
    st.write("BLA BLA BLA")

#########################################################################################################################

# Fonction pour le projet 6
def projet_6():
    st.title("Projet 6 : ")
    st.write("BLA BLA BLA")

#########################################################################################################################

# Fonction pour le projet 7
def projet_7():
    st.title("Projet 7 : ")
    st.write("BLA BLA BLA")

#########################################################################################################################

# Fonction pour le projet 8
def projet_8():
    st.title("Projet 8 : ")
    st.write("BLA BLA BLA")

#########################################################################################################################

# Fonction pour le projet 9
def projet_9():
    st.title("Projet 9 : ")
    st.write("BLA BLA BLA")

#########################################################################################################################

# Fonction pour la page de contact fusionnée
# Page de contact
def contact():
    # Informations personnelles
    st.subheader("**Mr Simunek Ludovic**")

    # Injecter le CSS pour styliser l'image en cercle
    st.markdown("""
    <style>
        .circle-img {
            border-radius: 50%;
            width: 200px;
            height: 200px;
            object-fit: cover;
        }
    </style>
    """, unsafe_allow_html=True)

    # Afficher l'image dans un cercle
    st.markdown('<img src="https://i72.servimg.com/u/f72/20/11/38/84/17014210.jpg" class="circle-img">', unsafe_allow_html=True)
    
    # Affichage des informations de contact
    st.write("Téléphone : 06 51 52 42 33")
    st.write("Email : ludovic@simunek.fr")
    st.write("[Profil Linkedin](https://www.linkedin.com/in/ludovic-simunek/)")

#########################################################################################################################

# Configuration de la barre latérale pour la navigation
pages = {
    "Accueil": accueil,
    "SQL & Power BI": projet_1,
    "Machine Learning": projet_2,
    "Geocodage": projet_3,
    "Projet 4": projet_4,
    "Projet 5": projet_5,
    "Projet 6": projet_6,
    "Projet 7": projet_7,
    "Projet 8": projet_8,
    "Projet 9": projet_9,
    "Contact": contact
}

# Sélection de la page via le widget sidebar
page_selection = st.sidebar.radio("Choisir une thématique :", list(pages.keys()))

# Affichage de la page choisie
pages[page_selection]()
