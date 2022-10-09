import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import FormSlice from 'api/slices/FormSlice';

export const store = configureStore({
  reducer: {
    counter: FormSlice,
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
