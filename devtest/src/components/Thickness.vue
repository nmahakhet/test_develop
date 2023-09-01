<template>
  <div class="flex flex-row flex-row-reverse mb-5">
    <v-btn @click="onCreateTp"
      ><v-icon start icon="mdi-plus-circle"></v-icon>Add Thickness</v-btn
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
      <tr v-for="(data, index) in thicknessDatas" :key="index">
        <td class="body-cell">{{ data.inspection_date }}</td>
        <td class="body-cell">{{ data.actual_thickness }}</td>
        <td class="body-cell actions">
          <span @click="onEditTp(data.id)"
            ><v-icon start icon="mdi-pencil-circle"></v-icon
          ></span>
          <span @click="onDeleteThickness(data.id)">
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
              v-model="createData.inspection_date"
              :label="formatLabel('inspection_date')"
            ></v-text-field>
            <v-text-field
              v-model="createData.actual_thickness"
              :label="formatLabel('actual_thickness')"
            ></v-text-field>
          </template>
          <template v-else>
            <v-text-field
              v-model="editData.inspection_date"
              :label="formatLabel('inspection_date')"
            ></v-text-field>
            <v-text-field
              v-model="editData.actual_thickness"
              :label="formatLabel('actual_thickness')"
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
import {
  getThickness,
  createThickness,
  updateThickness,
  deleteThickness,
} from "@/api/pipingApi";
import { useStore } from "vuex";

export default defineComponent({
  name: "ThicknessComponent",
  props: {
    id: {
      type: String,
      default: "1",
    },
  },
  data() {
    const headers: Array<string> = ["Inspection Date", "Actual Thickness(mm)"];
    const thicknessDatas: Array<any> = [];
    const now = new Date();

    // Format the date as 'YYYY-MM-DD' (or any desired format)
    const formattedDate = `${now.getFullYear()}-${(now.getMonth() + 1)
      .toString()
      .padStart(2, "0")}-${now.getDate().toString().padStart(2, "0")}`;
    const templateTpData = {
      inspection_date: formattedDate,
      actual_thickness: 0,
    };
    const editData = templateTpData;
    const createData = templateTpData;
    return {
      headers,
      thicknessDatas,
      dialog: false,
      editData,
      createData,
      templateTpData,
      idActive: 1,
      idTp: "1",
      searchQuery: "",
      typeDialog: "create",
      propertyNames: ["tp_number", "tp_description", "note"],
    };
  },
  async created() {
    const res = await getThickness(this.id);
    this.idTp = this.id;
    this.thicknessDatas = res;
  },
  methods: {
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
      const data = this.thicknessDatas.find((val) => val.id === id);
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
          inspection_date: this.createData.inspection_date,
          actual_thickness: this.createData.actual_thickness,
          test_point_id: this.idTp,
        };
        await createThickness(stucture);
      } else {
        const stucture = {
          inspection_date: this.editData.inspection_date,
          actual_thickness: this.editData.actual_thickness,
          test_point_id: this.idTp,
        };
        await updateThickness(this.idActive, stucture);
      }

      const res = await getThickness(this.idTp.toString());
      alert("Success");
      this.thicknessDatas = res;
      this.dialog = false;
      return;
    },
    async onDeleteThickness(id: any) {
      await deleteThickness(id);
      alert("Success");
      const res = await getThickness(this.idTp);
      this.thicknessDatas = res;
    },
  },
  watch: {
    async id() {
      const res = await getThickness(this.id);
      this.idTp = this.id;
      this.thicknessDatas = res;
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
