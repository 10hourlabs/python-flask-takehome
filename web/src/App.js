import * as React from "react";

function App() {
  return (
    <div className="w-6/12 mx-auto bg-gray-200 rounded-xl shadow border p-8 m-10">
      <h1 className="text-3xl text-gray-700 font-bold mb-5">
        Request a cleaner
      </h1>
      <div className="block p-6 rounded-lg shadow-lg bg-white w-full">
        <form>
          <div className="grid grid-cols-2 gap-4">
            <div className="form-group mb-6">
              <input
                type="text"
                className="form-control
          block
          w-full
          px-3
          py-1.5
          text-base
          font-normal
          text-gray-700
          bg-white bg-clip-padding
          border border-solid border-gray-300
          rounded
          transition
          ease-in-out
          m-0
          focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                id="exampleInput123"
                aria-describedby="emailHelp123"
                placeholder="Client Email Address"
              />
            </div>
            <div className="form-group mb-6">
              <select
                className="form-control
          block
          w-full
          px-3
          py-1.5
          text-base
          font-normal
          text-gray-700
          bg-white bg-clip-padding
          border border-solid border-gray-300
          rounded
          transition
          ease-in-out
          m-0
          focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                id="exampleInput124"
                aria-describedby="emailHelp124"
              >
                <option>Select Company</option>
                <option>Company ABC</option>
              </select>
            </div>
          </div>
          <div className="form-group mb-6">
            <select
              className="form-control block
        w-full
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        rounded
        transition
        ease-in-out
        m-0
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
              id="exampleInput125"
            >
              <option value="">Select Cleaner</option>
              <option value="">Cleaner A</option>
            </select>
          </div>
          <div className="form-group mb-6">
            <div className="flex justify-between border-b">
              <h4 className="font-bold">Shift</h4>
              <button className="bg-gray-600 py-2 px-10 rounded-md text-white text-sm hover:bg-gray-500">Add</button>
            </div>
            <div className="py-3">
              Select Date
            <input
                  type="date"
                  className="form-control block
        w-full
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        rounded
        transition
        ease-in-out
        m-0
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                  placeholder="Select Date"
                />
            </div>
            <div className="grid grid-cols-3 gap-4 pt-3">
              <div className="text-sm">Days</div>
              <div className="text-sm">Start Hours</div>
              <div className="text-sm">End Hours</div>
              <div className="text-sm font-bold">MON</div>
              <div className="">
                <input
                  type="time"
                  className="form-control block
        w-full
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        rounded
        transition
        ease-in-out
        m-0
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                  placeholder="Select"
                />
              </div>
              <div className="">
                <input
                  type="time"
                  className="form-control block
        w-full
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        rounded
        transition
        ease-in-out
        m-0
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                  placeholder="Select"
                />
              </div>
            </div>
          </div>
          <button
            type="submit"
            className="
      w-full
      px-6
      py-2.5
      bg-blue-600
      text-white
      font-medium
      text-xs
      leading-tight
      uppercase
      rounded
      shadow-md
      hover:bg-blue-700 hover:shadow-lg
      focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0
      active:bg-blue-800 active:shadow-lg
      transition
      duration-150
      ease-in-out"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  );
}

export default App;
