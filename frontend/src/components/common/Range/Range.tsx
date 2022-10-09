import { Range as RangeLibrary, getTrackBackground } from 'react-range';

import {  EFormLabels } from 'types';

import styles from './Range.module.scss';

type TRangeType = 'creditSum' | 'income';

interface IRangeProps {
    type: 'income' | 'creditSum';
    value: number;
    label: EFormLabels;
    min?: number;
    max?: number;
    onChange: (type: TRangeType, values: number) => void;
}

export const Range: React.FC<IRangeProps> = ({ type, min = 30000, max = 3000000, label, value, onChange}) => {
    const rangeBkgColor = ['rgba(95, 77, 130, 1)', 'rgba(239, 239, 246, 1)'];
    const step = 10000;
    return (
        <div className={styles.range}>
            <div className={styles.range__info}>
                <span className={styles.range__label}>{label}</span>
                <span className={styles.range__sum}>{value.toLocaleString('ru')} Р</span>
            </div>
            <RangeLibrary
                step={step}
                min={min}
                max={max}
                values={[value]}
                onChange={([values]) => onChange(type, values)}
                renderTrack={({ props, children }) => (
                    <div
                        onMouseDown={props.onMouseDown}
                        onTouchStart={props.onTouchStart}
                        className={styles.range__track}
                        >
                        <div
                            ref={props.ref}
                            className={styles.range__bkg}
                            style={{
                                background: getTrackBackground({
                                    values: [value],
                                    colors: rangeBkgColor,
                                    min,
                                    max
                                }),
                            }}
                        >
                            {children}
                        </div>
                    </div>
                )}
                renderThumb={({ props }) => (
                    <div
                        {...props}
                        className={styles.range__thumb}
                    />
                )}
            />
        </div>
    );
};
