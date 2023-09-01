import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "./assets/tailwind.css";
import VueSweetalert2 from "vue-sweetalert2";
import "sweetalert2/dist/sweetalert2.min.css";

const vuetify = createVuetify({
  components,
  directives,
});

const app = createApp(App);

app.use(store);
app.use(vuetify);
app.use(VueSweetalert2);
app.use(router);

app.mount("#app");
