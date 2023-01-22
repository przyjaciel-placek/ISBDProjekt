const routes=[
    {path:'/home',component:home},
    {path:'/employees',component:employees_list},
    {path:'/books',component:books_list}
]

const router=new VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
})

const app = Vue.createApp({})

app.use(router)
app.mount('#app')