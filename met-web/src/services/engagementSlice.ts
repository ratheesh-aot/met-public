import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const initialState: EngagementState = {
  allEngagements: [],
};

export const engagementSlice = createSlice({
  name: "engagement",
  initialState,
  reducers: {
    setEngagements: (state, action: PayloadAction<Engagement[]>) => {
      state.allEngagements = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setEngagements } = engagementSlice.actions;

export default engagementSlice.reducer;
