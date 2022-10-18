const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navbar-link')[0]

toggleButton.addEventListener('click', ()=>{
    navbarLinks.classList.toggle('active')
})



/* tickets */

function validation(){
    mail=document.getElementById("mail").value;
    if ( /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g.test(mail) ) {
        document.getElementById("mail").style="";
    }
    else {
        alert("Παρακαλώ ελέγξτε το πεδίο του email \nνα είναι της μορφής xxx@xxx.com/.gr. ");
        document.getElementById("mail").style="border:2px solid red;";
        document.getElementById("errors").innerText = "Το πεδίο του email είναι λάθος. \n";
        return false;
    }
    password=document.getElementById("password").value;
    if ( /^(?=.*\d)(?=.*[A-Z])(?!.*[^a-zA-Z0-9])(.{8,})$/.test(password) ) {
        document.getElementById("password").style="";
    }
    else {
        alert("Παρακαλώ ελέγξτε το πεδίο του password \nνα περιέχει από 8 χαρακτήρες και πάνω και τουλάχιστον \nένα κεφαλαίο γράμμα και έναν αριθμό. ");
        document.getElementById("password").style="border:2px solid red;";
        document.getElementById("errors").innerText += "Το πεδίο του password είναι λάθος. \n";
        return false;
    }
    firstname=document.getElementById("firstname").value;
    if (/^[a-zA-Z]+$/.test(firstname) ) {
        document.getElementById("firstname").style="";
    }
    else {
        alert("Παρακαλώ ελέγξτε το πεδίο του ονόματος \nνα περιέχει μόνον λατινικούς χαρακτήρες \nή να μην είναι κενό. ");
        document.getElementById("firstname").style="border:2px solid red;";
        document.getElementById("errors").innerText += "Το πεδίο του ονόματος είναι λάθος. \n";
        return false;
    }
    lastname=document.getElementById("lastname").value;
    if (/^[a-zA-Z]+$/.test(lastname) ) {
        document.getElementById("lastname").style="";
    }
    else {
        alert("Παρακαλώ ελέγξτε το πεδίο του επωνύμου \nνα περιέχει μόνον λατινικούς χαρακτήρες \nή να μην είναι κενό. ");
        document.getElementById("lastname").style="border:2px solid red;";
        document.getElementById("errors").innerText += "Το πεδίο του επωνύμου είναι λάθος. \n";
        return false;
    }
    address=document.getElementById("address").value;
    if (/^[a-zA-Z]+$/.test(address) ) {
        document.getElementById("address").style="";
        document.getElementById("errors").innerText += "Το πεδίο της διεύθυνσης είναι λάθος. \n";	
    }
    else {
        alert("Παρακαλώ ελέγξτε το πεδίο της διεύθυνσης \nνα περιέχει αλφαριθμιτικούς χαρακτήρες \nή να μην είναι κενό. ");
        document.getElementById("address").style="border:2px solid red;";
        document.getElementById("errors").innerText += "Το πεδίο της διεύθυνσης είναι λάθος. \n";
        return false;
    }
    zip=document.getElementById("zip").value;
    if ( /^[0-9]{5,5}$/.test(zip) ) {
        document.getElementById("zip").style="" ;
    }
    else {
        alert("Παρακαλώ ελέγξτε το πεδίο του ταχυδρομικού κώδικα \nνα περιέχει ακριβώς 5 αριθμούς. ");
        document.getElementById("zip").style="border:2px solid red;";
        document.getElementById("errors").innerText += "Το πεδίο του ταχυδρομικού κώδικα είναι λάθος. \n";
        return false;
    }
    phone=document.getElementById("phone").value;
    if (/^[0-9]{12,12}$/.test(phone) ) {
        document.getElementById("phone").style="";
    }
    else {
        alert("Παρακαλώ ελέγξτε το πεδίο του αριθμού τηλεφώνου \nνα περιέχει ακριβώς 12 αριθμούς. ");
        document.getElementById("phone").style="border:2px solid red;";
        document.getElementById("errors").innerText += "Το πεδίο του αριθμού τηλεφώνου είναι λάθος. \n";
        return false;				
    }
    card_num=document.getElementById("card_num").value;
    if (/^[0-9]{16,16}$/.test(card_num) ) {
        document.getElementById("card_num").style="";
    }
    else {
        alert("Παρακαλώ ελέγξτε το πεδίο του αριθμού πιστωτικής κάρτας \nνα περιέχει ακριβώς 16 αριθμούς. ");
        document.getElementById("card_num").style="border:2px solid red;";
        document.getElementById("errors").innerText += "Το πεδίο του αριθμού πιστωτικής κάρτας είναι λάθος. \n";
        return false;
    }
}
document.getElementById("button").addEventListener("click", function (){validation()});


