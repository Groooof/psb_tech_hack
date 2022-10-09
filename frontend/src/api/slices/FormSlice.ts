import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
//ESlint не воспринимает type и обычный импорт раздельно
// eslint-disable-next-line no-duplicate-imports
import type { PayloadAction } from '@reduxjs/toolkit';
import { postData } from 'api/ApiService';
import { IPostDataEntity, IResponseEntity } from 'api/types';

import { initialState  } from 'api/const/FormConstants';
import { IFormValues } from 'types';


const postUserData = createAsyncThunk(
    'form/postUserData',
    async (data: IPostDataEntity) => {
        const response = await postData(data);
        const jsonData: IResponseEntity = await response.json();
        return jsonData;
    }
);

const counterSlice = createSlice({
    name: 'form',
    initialState,
    reducers: {
        updateField(state, action: PayloadAction<IFormValues>) {
            state.userData = action.payload;
        }
    }, extraReducers(builder) {
        builder.addCase(postUserData.fulfilled, (state, action) => {
            state.min_overpayment = action.payload.min_overpayment;
            state.min_monthly_payment = action.payload.min_monthly_payment;
            
        });
        builder.addCase(postUserData.rejected, (state, action) => {
            state.loading = 'failed';
            console.error(action.payload);
        });
    },
});


export const { updateField } = counterSlice.actions;
export default counterSlice.reducer;