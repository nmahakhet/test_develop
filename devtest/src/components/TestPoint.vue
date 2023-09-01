<template>
  <div class="flex flex-row flex-row-reverse mb-5">
    <v-btn @click="onCreateTp"
      ><v-icon start icon="mdi-plus-circle"></v-icon>Add Testpoint</v-btn
    >
  </div>
  <v-table class="border-collapse">
    <thead>
      <tr>
        <th
          v-for="(header, index) in headers"
          :key="index"
          class="header-cell text-center text-white"
        >
          {{ header }}
        </th>
        <th class="header-cell text-center text-white"></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(data, index) in tpDatas" :key="index">
        <td class="body-cell">{{ data.tp_number }}</td>
        <td class="body-cell">{{ data.tp_description }}</td>
        <td class="body-cell">{{ data.note }}</td>
        <td class="body-cell actions">
          <span @click="onEditTp(data.id)"
            ><v-icon start icon="mdi-pencil-circle"></v-icon
          ></span>
          <span @click="onDeleteTp(data.id)">
            <v-icon start icon="mdi-delete-circle"></v-icon>
          </span>
        </td>
      </tr>
    </tbody>
  </v-table>
  <v-dialog v-model="dialog" width="800">
    <v-card>
      <v-card-title>
        <span class="text-h5">Info</span>
      </v-card-title>
      <v-card-text>
        <form @submit.prevent="submit">
          <template v-if="typeDialog === 'create'">
            <v-text-field
              v-model="createData.tp_number"
              :label="formatLabel('tp_number')"
            ></v-text-field>
            <v-text-field
              v-model="createData.tp_description"
              :label="formatLabel('tp_description')"
            ></v-text-field>
            <v-text-field
              v-model="createData.note"
              :label="formatLabel('note')"
            ></v-text-field>
          </template>
          <template v-else>
            <v-text-field
              v-model="editData.tp_number"
              :label="formatLabel('tp_number')"
            ></v-text-field>
            <v-text-field
              v-model="editData.tp_description"
              :label="formatLabel('tp_description')"
            ></v-text-field>
            <v-text-field
              v-model="editData.note"
              :label="formatLabel('note')"
            ></v-text-field>
          </template>

          <v-btn color="green-darken-1" class="me-4" type="submit">
            submit
          </v-btn>
        </form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { getTp, createTp, updateTp, deleteTp } from "@/api/pipingApi";
import { useStore, mapActions } from "vuex";

export default defineComponent({
  name: "TestPointComponent",
  props: {
    id: {
      type: String,
      default: "1",
    },
  },
  data() {
    const headers: Array<string> = ["TP number", "TP Description", "Note"];
    const tpDatas: Array<any> = [];
    const templateTpData = {
      tp_number: 0,
      tp_description: 0,
      note: 0,
    };
    const editData = templateTpData;
    const createData = templateTpData;
    return {
      headers,
      tpDatas,
      dialog: false,
      editData,
      createData,
      templateTpData,
      idActive: 1,
      idCml: "1",
      searchQuery: "",
      typeDialog: "create",
      propertyNames: ["tp_number", "tp_description", "note"],
    };
  },
  async mounted() {
    const res = await getTp(this.id);
    this.idCml = this.id;
    this.setTestPoint(res);
    this.tpDatas = res;
  },
  methods: {
    ...mapActions(["setTestPoint"]),
    back() {
      this.$router.push({ name: "piping" });
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
    onCreateTp() {
      this.typeDialog = "create";
      this.createData = this.templateTpData;
      this.dialog = true;
    },
    async onEditTp(id: number) {
      this.typeDialog = "edit";
      const data = this.tpDatas.find((val) => val.id === id);
      this.editData = JSON.parse(JSON.stringify(data));
      this.idActive = id;
      this.dialog = true;
    },
    formatLabel(property: string) {
      // Replace underscores with spaces and capitalize the property name
      return property.replace(/_/g, " ").toUpperCase();
    },
    async submit() {
      if (this.typeDialog === "create") {
        const stucture = {
          tp_number: Number(this.createData.tp_number),
          tp_description: this.createData.tp_description,
          note: this.createData.note,
          cml_id: this.idCml,
        };
        await createTp(stucture);
      } else {
        const stucture = {
          tp_number: Number(this.editData.tp_number),
          tp_description: this.editData.tp_description,
          note: this.editData.note,
          cml_id: this.idCml,
        };
        await updateTp(this.idActive, stucture);
      }
      alert("Success");
      const res = await getTp(this.idCml.toString());
      this.tpDatas = res;
      this.dialog = false;
      return;
    },
    async onDeleteTp(id: any) {
      await deleteTp(id);
      alert("Success");
      const res = await getTp(this.idCml);
      this.setTestPoint(res);
      this.tpDatas = res;
    },
  },
  watch: {
    async id() {
      const res = await getTp(this.id);
      this.idCml = this.id;
      this.setTestPoint(res);
      this.tpDatas = res;
    },
  },
});
</script>
<style scoped>
.border-collapse {
  border-collapse: collapse;
  width: 100%; /* Ensure table width spans the container */
}

.header-cell {
  background-color: #3490dc; /* Header cell background color */
  color: #ffffff; /* Header cell text color */
  padding: 0.5rem;
  text-align: center; /* Center-align text in header cells */
}

.body-row:hover {
  background-color: #e2e8f0; /* Body row background color on hover */
}

.body-cell {
  padding: 0.5rem;
}

.actions span {
  cursor: pointer;
  color: #3490dc; /* Action link color */
  margin-right: 1rem;
}

.actions span:hover {
  text-decoration: underline; /* Underline the action link on hover */
  color: #2779bd; /* Hovered action link color */
}
</style>
