const employee_log={template:`

<h1>Logowanie na konto pracownika</h1>

<div>
<div class="input-group mb-3">
            <span class="input-group-text">Login</span>
            <input type="text" class="form-control" v-model="LoginP">
</div>
<div class="input-group mb-3">
            <span class="input-group-text">Hasło</span>
            <input type="password" class="form-control" v-model="HasloP">
</div>

<button type="button"
class="btn btn-primary m-2 fload-end"
data-bs-toggle="modal"
data-bs-target="#exampleModal"
@click="logClick()">
    Zaloguj
</button>

</div>

`,

data(){
    return{
        LoginP:"",
        HasloP:""
    }
},
methods:{
    async logClick(){
        try {
            const response = await axios.get(variables.API_URL+"pracownik");
            for (const user of response.data) {
              if (user.LoginP === this.LoginP && user.HasloP === this.HasloP) {
                alert("Zalogowano pomyślnie");
                window.location.href = 'file:///C:/Users/dziez/Desktop/5/bd/aplikacja/KsiegarniaInternetowa/ui/index.html#';
                return true;
              }
            }
            alert("Błędny login lub hasło");
            return false;
          } catch (error) {
            console.log(error);
          } 
    }
}}