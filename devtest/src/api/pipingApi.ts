import ApiService from "./Apiservice";

export async function getInfo(): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: "/info",
      method: "GET",
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function getCml(id: string): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/cml/${id}`,
      method: "GET",
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function updateInfo(id: number, data: string): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/update_info/${id}`,
      method: "PUT",
      data: data,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function createInfo(data: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/insert_info`,
      method: "POST",
      data: data,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function createCml(data: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/insert_cml`,
      method: "POST",
      data: data,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function updateCml(id: number, data: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/update_cml/${id}`,
      method: "PUT",
      data: data,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function createTp(data: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/insert_testpoint`,
      method: "POST",
      data: data,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function updateTp(id: number, data: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/update_testpoint/${id}`,
      method: "PUT",
      data: data,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function getTp(id: string): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/testpoint/${id}`,
      method: "GET",
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function getThickness(id: string): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/thickness/${id}`,
      method: "GET",
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function createThickness(data: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/insert_thickness`,
      method: "POST",
      data: data,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function updateThickness(id: number, data: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/update_thickness/${id}`,
      method: "PUT",
      data: data,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function deleteInfo(id: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/delete_info/${id}`,
      method: "DELETE",
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function deleteCml(id: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/delete_cml/${id}`,
      method: "DELETE",
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function deleteTp(id: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/delete_testpoint/${id}`,
      method: "DELETE",
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

export async function deleteThickness(id: any): Promise<any> {
  // eslint-disable-next-line no-useless-catch
  try {
    const response = await ApiService.request({
      url: `/delete_thickness/${id}`,
      method: "DELETE",
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}
