import Image from "next/image";
import socialmedia from "@/public/socicalmedia.svg";
import contentcreator from "@/public/contentcreator.png";
import bubbleicon from "@/public/SocialMedia/bubble.svg";
import webflow from "@/public/SocialMedia/webflow.svg";
import Wixicon from "@/public/SocialMedia/wix.svg";
import framer from "@/public/SocialMedia/framer.svg";
import resume from "@/public/resume.png";
import techstack from "@/public/techstack.png";
import NoGenAI from "@/components/(SocialMedia)/NoGenAI";
import mainresume from "@/public/MainResume.svg";


import NoCodeDevCard from "@/components/(SocialMedia)/NoCodeDevCard";
export function SocialMedia() {
  return (
    <div className="max-w-7xl mx-auto px-4 py-12 sm:px-6 lg:px-8 font-['Outfit']">
      <div className="text-center mb-16 font-medium">
        <p className="text-2xl md:text-[53px] md:leading-[60px] md:pt-[228px] pt-6 ">
          Your premium Space to <br />
          <span className="block md:inline">Learn, Connect, and Excel!</span>
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-12 gap-4 md:gap-6 md:mx-[19px]">
        <div className="bg-[#FFBF00] rounded-2xl p-6 md:p-8 flex flex-col md:col-span-4 md:row-span-2">
          <h2 className="text-[31px] font-bold text-[#5C3F00]">Career Ready</h2>

          <div className="flex-grow flex items-center justify-center my-6 relative group">
  {/* Main Image - Rotates slightly left */}
  <Image
    src={mainresume}
    alt="do"
    width={205}
    height={300}
    className="relative transition-transform duration-300 group-hover:-rotate-3"
  />

  {/* Second Image - Rotates slightly right */}
  <Image
    src={resume}
    alt="Resume templates"
    width={230}
    height={300}
    className="absolute ml-20 mt-3 object-contain transition-transform duration-300 group-hover:rotate-3"
  />
</div>
    


          <p className="text-lg mt-auto text-[#5C3F00]">
            Ace your resume and interviews to land <br /> your dream job.
          </p>
        </div>

        <div className="bg-[#77D4D1] rounded-2xl p-6 md:py-10 md:col-span-8">
          <div className="flex flex-col md:flex-row justify-evenly ">
            <div className="md:mt-6">
              <h2 className="text-[31px]  font-bold mb-2 pt-14">
                Social Connect
              </h2>
              <p className="text-sm md:text-xl leading-6">
                Build your brand and <br /> network to shine online.
              </p>
            </div>
            <div className="flex justify-center md:justify-end mt-4 md:mt-0">
              <Image
                src={socialmedia}
                alt="Social networking illustration"
                width={410}
                className="object-contain"
              />
            </div>
          </div>
        </div>

        <div className="bg-[#12100E] text-white rounded-2xl p-6 md:p-[48px] md:col-span-4">
          <div className="flex flex-col h-full">
            <div className="flex-grow flex items-center justify-center">
              <Image
                src={contentcreator}
                alt="Content creation illustration"
                width={272}
                height={500}
                className="object-contain"
              />
            </div>
            <div className="mt-auto">
              <h2 className="text-[31px] pt-[24px] font-bold mb-2 ">
                Content Creation
              </h2>
              <p className="text-sm md:text-xl">
                Master the art of creating engaging content.
              </p>
            </div>
          </div>
        </div>
        <NoCodeDevCard
          framer={framer}
          bubbleicon={bubbleicon}
          webflow={webflow}
          Wixicon={Wixicon}
        />

        <div className="bg-[#66CEF5] rounded-2xl p-6 md:p-8 md:col-span-8">
          <div className="flex flex-col md:flex-row md:items-center h-full">
            <div className="md:w-1/2 mt-auto py-[48px]">
              <h2 className="text-[31px] font-bold mb-2">Tech Stacks</h2>
              <p className="text-sm md:text-xl">
                Break down complex tech <br /> trends into clear insights.
              </p>
            </div>
            <div className=" flex justify-center md:justify-end mt-4 md:mt-0">
              <Image
                src={techstack}
                alt="Tech stack logos"
                width={622}
                className="object-contain"
              />
            </div>
          </div>
        </div>

  
        <div className="bg-[#966FD6] rounded-2xl p-6 md:p-8 md:col-span-4">
          <NoGenAI />
        </div>
      </div>
    </div>
  );
}
