const client_log={template:`

<h1>Logowanie na konto klienta</h1>

<div>
<div class="input-group mb-3">
            <span class="input-group-text">Login</span>
            <input type="text" class="form-control" v-model="LoginK">
</div>
<div class="input-group mb-3">
            <span class="input-group-text">Hasło</span>
            <input type="password" class="form-control" v-model="HasloK">
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
        LoginK:"",
        HasloK:""
    }
},
methods:{
    async logClick(){
        try {
            const response = await axios.get(variables.API_URL+"klient");
            for (const user of response.data) {
              if (user.LoginK === this.LoginK && user.HasloK === this.HasloK) {
                alert("Zalogowano pomyślnie");
                window.location.href = 'file:///C:/Users/dziez/Desktop/5/bd/aplikacja/KsiegarniaInternetowa/ui/client_view.html#';
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